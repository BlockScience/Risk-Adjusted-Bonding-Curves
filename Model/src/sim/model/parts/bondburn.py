from .choose_action import *
#from ..import bonding_curve_eq

# Include this function as another part so as to account for all mechansims (?)
# don't require this because handling with amounts (0 vs +ve) instead of action performed
'''def action_taken():
    if action['mech'] == 'bond':
        dS, pbar = bond(amt_to_bond, R, S, V, params['kappa'])
    elif action['mech'] == 'burn': 
        dR, pbar = withdraw(amt_to_burn, R, S, V, params['kappa'])
    else:
        print("No bond or burn made")
    return #?????? '''


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
        deltaR = R-((S-deltaS)**kappa)/V
        R = R + policy_input['amt_to_bond'] - deltaR
        print("RESERVE = ", R, " | deltaR = ", deltaR, " | deltaS = ", deltaS)

    return 'reserve', R


def update_S(params, substep, state_history, prev_state, policy_input):
    #action = _input['action']
    #deltaR = _input['amt_to_bond']
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    kappa = prev_state['kappa']
    deltaR = policy_input['amt_to_bond']

    deltaS = (V*(R+deltaR))**(1/kappa)-S
    S = S - deltaS + policy_input['amt_to_burn']
    print("SUPPLY = ", S, " | deltaR = ", deltaR, " | deltaS = ", deltaS)

    return 'supply', S


def update_r(params, substep, state_history, prev_state, policy_input):
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    kappa = prev_state['kappa']
    r = prev_state['agent_reserve']
    deltaS = policy_input['amt_to_burn']

    if V == 0:
        print("V IS ZERO")
    else:
        deltar = R-((S-deltaS)**kappa)/V

    r = r - policy_input['amt_to_bond'] + deltar
    print("AGENT RESERVE =", r, "deltar = ", deltar,
          "policy_input['amt_to_bond'] = ", policy_input['amt_to_bond'])
    return 'agent_reserve', r


def update_s_bondburn(params, substep, state_history, prev_state, policy_input):
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    kappa = prev_state['kappa']
    s = prev_state['agent_supply']
    deltaR = policy_input['amt_to_bond']

    deltas = (V*(R+deltaR))**(1/kappa)-S

    s = s + deltas - policy_input['amt_to_burn']
    print("AGENT SUPPLY =", s, "deltas = ", deltas,
          "policy_input['amt_to_burn'] = ", policy_input['amt_to_burn'])
    return 'agent_supply', s


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

    print("SPOT PRICE P (from bondburn update) = ", P)
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
    elif deltaR == 0:
        deltaR = R-((S-deltaS)**kappa)/V

    realized_price = deltaR/deltaS
    pbar = realized_price
    print("PRICE pbar (from bondburn update) =", pbar)
    return 'price', pbar


def update_I_bondburn(params, substep, state_history, prev_state, policy_input):
    R = prev_state['reserve']
    C = params['C']
    alpha = prev_state['alpha']
    deltaR = policy_input['amt_to_bond']

    I = (R + deltaR) + (C*alpha)
    print("C =", C, "alpha = ", alpha, "R = ", R, "deltaR = ", deltaR)
    print("I (from bondburn) =", I)
    print("--------------------------------------")
    return 'invariant_I', I

# kappa does not change
# def update_kappa(_params, substep, state_history, prev_state, _input):
#    kappa = kappa(deltaR, R, S, V, I, alpha)
#    return 'kappa', kappa


""" def log(self, parameter_list):
    if(degub)
 """
'''
if action['mech'] == 'bond':
        dS, pbar = bond(amt_b, R, S, V, params['kappa'])
        R = R + amt_b
        S = S + dS
        I = R + (C*alpha)
        kappa = kappa(deltaR, R, S, V, I, alpha)
        P = spot_price(R, V, kappa)
        

elif action['mech'] == 'burn':
        dR, pbar = withdraw(amt_b, R, S, V, params['kappa'])
        R = R - dR
        S = S - amt_b
        I = R + (C*alpha)
        kappa = kappa(dR, R, S, V, I, alpha)
        P = spot_price(R, V, kappa)
'''
