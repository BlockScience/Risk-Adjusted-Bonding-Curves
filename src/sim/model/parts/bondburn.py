#from ..import bonding_curve_eq

# Include this function as another part so as to account for all mechansims (?)
# don't require this because handling with amounts (0 vs +ve) instead of action performed


def update_R(params, substep, state_history, prev_state, policy_input):
    #action = _input['action']
    #deltaS = _input['amt_to_burn']
    # access amt_to_burn using _input['action']['amt_to_burn'] because it's a dict of dicts
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    # print("invariant_V = ", V)
    kappa = prev_state['kappa']
    deltaS = policy_input['amt_to_burn']

    if V == 0:
        print("V IS ZERO")  # degenerate
    else:
        deltaR = (((S-deltaS)**kappa)/V) - R
        R = R + policy_input['amt_to_bond'] - deltaR
        # print("RESERVE = ", R, " | deltaR = ", deltaR, " | deltaS = ", deltaS)

    return 'reserve', R


def update_S(params, substep, state_history, prev_state, policy_input):
    #action = _input['action']
    #deltaR = _input['amt_to_bond']
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    kappa = prev_state['kappa']
    deltaR = policy_input['amt_to_bond']

    deltaS = S - (V*(R+deltaR))**(1/kappa)
    S = S - deltaS + policy_input['amt_to_burn']
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

    # print("AGENT SUPPLY =", s_free, "deltas = ", deltas,
    # "policy_input['amt_to_burn'] = ", policy_input['amt_to_burn'])
    return 'agent_supply_free', s_free


def compute_r(R, S, V, kappa, r, deltaS, policy_input):
    if V == 0:
        print("V IS ZERO")
    else:
        deltar = R-((S-deltaS)**kappa)/V

    r = r - policy_input['amt_to_bond'] + deltar
    return r


def compute_s_free(R, S, V, kappa, s_free, deltaR, policy_input):
    deltas = (V*(R+deltaR))**(1/kappa)-S

    s_free = s_free + deltas - policy_input['amt_to_burn']
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

    agent['agent_reserve'] = compute_r(R, S, V, kappa, r, deltaS, policy_input)
    agent['agent_supply_free'] = compute_s_free(
        R, S, V, kappa, s_free, deltaR, policy_input)

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
    elif amt_to_burn > 0:  # burn
        deltaS = amt_to_burn
        deltaR = R-((S-deltaS)**kappa)/V

    if amt_to_burn == 0:
        P = kappa*(R**((kappa-1.0)/kappa)/(float(V) **
                                           (1.0/float(kappa))))  # Zero handling
    else:
        P = amt_to_bond/amt_to_burn  # deltaR/deltaS

    # print("SPOT PRICE P (from bondburn update) = ", P)
    return 'spot_price', P


"""     R = prev_state['reserve']
    V = prev_state['invariant_V']
    kappa = prev_state['kappa']

    P = spot_price(R, V, kappa) """


def update_pbar(params, substep, state_history, prev_state, policy_input):
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    kappa = prev_state['kappa']
    deltaS = policy_input['amt_to_burn']
    deltaR = policy_input['amt_to_bond']

    if deltaS == 0:
        deltaS = (V*(R+deltaR))**(1/kappa)-S
   ############ STILL DIVISION by ZERO #######################
        if deltaS == 0:
            deltaS = 0.00001
        ############ STILL DIVISION by ZERO #######################
    elif deltaR == 0:
        deltaR = R-((S-deltaS)**kappa)/V

    realized_price = deltaR/deltaS
    pbar = realized_price
    print("PRICE pbar (from bondburn update) =", pbar)
    return 'price', pbar


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
