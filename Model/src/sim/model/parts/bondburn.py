from .choose_action import *
from ..import bonding_curve_eq

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
    print("policy_input = ", policy_input)
    print("policy_input['action'] = ", policy_input['action'])
    deltaS = policy_input['amt_to_burn']

    deltaR = R-((S-deltaS)**kappa)/V0
    R = R + policy_input['amt_to_bond'] - deltaR
    print("RESERVE = ", R)

    return 'reserve', R


def update_S(params, substep, state_history, prev_state, policy_input):
    #action = _input['action']
    #deltaR = _input['amt_to_bond']
    deltaR = policy_input['amt_to_bond']

    deltaS = (V0*(R+deltaR))**(1/kappa)-S
    S = S + deltaS - policy_input['amt_to_burn']

    return 'supply', S


def update_price(params, substep, state_history, prev_state, policy_input):
    amt_to_bond = policy_input['amt_to_bond']
    amt_to_burn = policy_input['amt_to_burn']
    kappa = prev_state['kappa']
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['V']

    if amt_to_bond > 0:  # bond
        deltaR = amt_to_bond
        deltaS = (V0*(R+deltaR))**(1/kappa)-S
    elif amt_to_burn > 0:  # burn
        deltaS = amt_to_burn
        deltaR = deltaR = R-((S-deltaS)**kappa)/V0

    if deltaS == 0:
        P = kappa*(R**((kappa-1)/kappa)/V0**(1/kappa))
    else:
        P = deltaR/deltaS

    return 'price', P


"""     R = prev_state['reserve']
    V = prev_state['invariant_V']
    kappa = prev_state['kappa']

    P = spot_price(R, V, kappa) """


def update_pbar(params, substep, state_history, prev_state, policy_input):
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['V']
    deltaS = policy_input['amt_to_burn']
    deltaR = policy_input['amt_to_bond']

    if deltaS == 0:
        deltaS = (V*(R+deltaR))**(1/kappa)-S
    elif deltaR == 0:
        deltaR = R-((S-deltaS)**kappa)/V

    realized_price = deltaR/deltaS
    pbar = realized_price
    return 'realized_price', pbar


def update_I(params, substep, state_history, prev_state, policy_input):
    R = prev_state['reserve']
    C = _params['C']
    alpha = prev_state['alpha']
    delta_R = policy_input['amt_to_burn']

    I = (R + deltaR) + (C*alpha)
    return 'invariant_I', I

# kappa does not change
# def update_kappa(_params, substep, state_history, prev_state, _input):
#    kappa = kappa(deltaR, R, S, V, I, alpha)
#    return 'kappa', kappa


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
