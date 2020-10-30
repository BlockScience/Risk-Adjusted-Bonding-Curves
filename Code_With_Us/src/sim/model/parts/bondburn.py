

def update_R(params, substep, state_history, prev_state, policy_input):
    # params = params[0]
    # access amt_to_burn using _input['action']['amt_to_burn'] because it's a dict of dicts
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']

    kappa = prev_state['kappa']
    deltaS = policy_input['amt_to_burn']

    if V == 0:
        print("V IS ZERO")  # degenerate
    else:
        deltaR = R - (((S-deltaS)**kappa)/V)
        #print("::::delta R::::", deltaR)
        #print("::::AMTBOND::::", policy_input['amt_to_bond'])

        ## Continuous ##
        # Continuous Enabled, newly reserved funds split to bond reserve and project funding
        if params['ENABLE_CONTINUOUS']:
            R = R + policy_input['amt_to_bond']*(1-params['THETA']) # - deltaR  all burned funds not tempered by theta
            if params['ENABLE_BURN']:
                R = R  - deltaR # for burning allowed (=TRUE) subtract burned funds from reserve
                
        # Continuous Not Enabled, all new reserve funds go to reserve the bond
        else:
            if params['ENABLE_BURN']:
                R = R + policy_input['amt_to_bond'] - deltaR # for burning allowed (=TRUE) subtract burned funds from reserve
            else:
                R = R + policy_input['amt_to_bond'] # for burning on bodning curve not allowed, occurs in uniswap
        # print("RESERVE = ", R, " | deltaR = ", deltaR, " | deltaS = ", deltaS)

    return 'reserve', R

def update_funds(params, substep, state_history, prev_state, policy_input):
    # params = params[0]
    # access amt_to_burn using _input['action']['amt_to_burn'] because it's a dict of dicts
    F = prev_state['funds_from_bond']
    V = prev_state['invariant_V']
    monthly_instalment = policy_input['monthly_instalment']
    
    if V == 0:
        print("V IS ZERO")  # degenerate
    else:
        ## Continuous ##
        if params['ENABLE_CONTINUOUS']:
            deltaF = policy_input['amt_to_bond'] * (params['THETA']) 

            # burn if else

        else:
            deltaF = 0

    F += deltaF
    F += monthly_instalment
    return 'funds_from_bond', F

def update_S(params, substep, state_history, prev_state, policy_input):
    # params = params[0]
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    kappa = prev_state['kappa']
    deltaR = policy_input['amt_to_bond']

    deltaS = (V*(R+deltaR))**(1/kappa) - S
    # S = S - deltaS + policy_input['amt_to_burn']
    # ?????????????????? Backwards ????????????????????

    S = S + deltaS - policy_input['amt_to_burn']
    # print("SUPPLY = ", S, " | deltaR = ", deltaR, " | deltaS = ", deltaS)

    return 'supply', S


def update_r(params, substep, state_history, prev_state, policy_input):
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    kappa = prev_state['kappa']
    r = prev_state['chosen_agent']['agent_reserve']
    deltaS = policy_input['amt_to_burn']

    if V == 0:
        print("V IS ZERO")
    else:
        deltar = R-((S-deltaS)**kappa)/V

    r = r - policy_input['amt_to_bond'] + deltar

    # print("AGENT RESERVE =", r, "deltar = ", deltar,
    # "policy_input['amt_to_bond'] = ", policy_input['amt_to_bond'])
    return 'agent_reserve', r


def update_s_free_bondburn(params, substep, state_history, prev_state, policy_input):
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    kappa = prev_state['kappa']
    s_free = prev_state['agent_supply_free']
    deltaR = policy_input['amt_to_bond']

    deltas = (V*(R+deltaR))**(1/kappa)-S

    s_free = s_free + deltas - policy_input['amt_to_burn']

    return 'agent_supply_free', s_free


def compute_r(R, S, V, kappa, r, deltaS, policy_input):
    if V == 0:
        r = policy_input['amt_to_bond']
    else:
        deltar = R-((S-deltaS)**kappa)/V
        r = r - policy_input['amt_to_bond'] + deltar
    return r


def compute_s_free(R, S, V, kappa, s_free, deltaR, policy_input, timestep):

    deltas = (V*(R+deltaR))**(1/kappa)-S

    s_free = s_free + deltas - policy_input['amt_to_burn']

    # TEST RANDOM DROP
    if timestep % 20 == 0:
        random_drop = 0
    else:
        random_drop = 0

    s_free = s_free + random_drop

    return s_free


def update_agent_BC(params, substep, state_history, prev_state, policy_input):
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    kappa = prev_state['kappa']

    agent = prev_state['chosen_agent']
    r = agent['agent_reserve']
    s_free = agent['agent_supply_free']

    deltaS = policy_input['amt_to_burn']
    deltaR = policy_input['amt_to_bond']

    timestep = prev_state['timestep']

    agent['agent_reserve'] = compute_r(R, S, V, kappa, r, deltaS, policy_input)

    agent['agent_supply_free'] = compute_s_free(
        R, S, V, kappa, s_free, deltaR, policy_input, timestep)

    return 'chosen_agent', agent


def update_P_bondburn(params, substep, state_history, prev_state, policy_input):
    amt_to_bond = policy_input['amt_to_bond']
    amt_to_burn = policy_input['amt_to_burn']
    kappa = prev_state['kappa']
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']

    if amt_to_bond > 0:  # bond
        deltaR = amt_to_bond
        deltaS = (V*(R+deltaR))**(1/kappa)-S

        if deltaS == 0:
            P = kappa*(R**((kappa-1.0)/kappa)/(float(V) **
                                               (1.0/float(kappa))))  # Zero handling
            # return 'spot_price', P
        else:
            P = deltaR/deltaS  # deltaR/deltaS
            # return 'spot_price', P

    elif amt_to_burn > 0:  # burn
        deltaS = amt_to_burn
        deltaR = R - (((S-deltaS)**kappa)/V)

        if deltaS == 0:
            P = kappa*(R**((kappa-1.0)/kappa)/(float(V) **
                                               (1.0/float(kappa))))  # Zero handling
            # return 'spot_price', P
        else:
            P = deltaR/deltaS  # deltaR/deltaS
            # return 'spot_price', P

    elif amt_to_burn == 0:
        P = kappa*(R**((kappa-1.0)/kappa)/(float(V) **
                                           (1.0/float(kappa))))  # Zero handling

    elif amt_to_bond == 0:
        P = prev_state['spot_price']

    else:
        P = amt_to_bond/amt_to_burn

    #print("PRICE (BOND/BURN): ", P)
    # print("SPOT PRICE P (from bondburn update) = ", P)
    return 'spot_price', P


def update_pbar(params, substep, state_history, prev_state, policy_input):
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    kappa = prev_state['kappa']
    deltaS = policy_input['amt_to_burn']
    deltaR = policy_input['amt_to_bond']

    if deltaS != 0:
        deltaR = R-((S-deltaS)**kappa)/V
        if deltaR == 0:
            realized_price = prev_state['pbar']
        else:
            realized_price = deltaR/deltaS
    elif deltaR != 0:
        deltaS = (V*(R+deltaR))**(1/kappa)-S
        if deltaS == 0:
            realized_price = prev_state['pbar']
        else:
            realized_price = deltaR/deltaS
    else:
        realized_price = prev_state['pbar']

    # print("PRICE pbar (from bondburn update) =", realized_price)
    return 'pbar', realized_price


def update_I_bondburn(params, substep, state_history, prev_state, policy_input):
    # params = params[0]
    R = prev_state['reserve']
    C = params['C']
    alpha = prev_state['alpha']
    deltaR = policy_input['amt_to_bond']

    I = (R + deltaR) + (C*alpha)
    #print("C =", C, "alpha = ", alpha, "R = ", R, "deltaR = ", deltaR)
    #print("I (from bondburn) =", I)
    # print("--------------------------------------")
    return 'invariant_I', I
