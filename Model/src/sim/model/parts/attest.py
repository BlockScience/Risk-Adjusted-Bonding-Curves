from .choose_action import *

# Include this function as another part so as to account for all mechansims (?)
# don't require this because handling with amounts (0 vs +ve) instead of action performed
'''def action_taken():
    action = _input['action']
    if action['mech'] == 'attest_pos':
        S1 = prev_state['supply_1']
        dQ1, alpha_belief = attest_pos(amt_pos, S1, C, I, params['kappa'])
    elif action['mech'] == 'attest_neg':       
        dQ0, alpha_belief = attest_neg(amt_neg, S0, C, I, params['kappa'])
    return '''


def update_S1(params, substep, state_history, prev_state, policy_input):
    #action = _input['action']
    S1 = prev_state['supply_1']
    # amt_pos is a key in a dict of dicts
    amt_pos = policy_input['action']['amt_pos']

    S1 = S1 + amt_pos
    return 'supply_1', S1


def update_S0(params, substep, state_history, prev_state, policy_input):
    S0 = prev_state['supply_0']
    amt_neg = policy_input['action']['amt_neg']

    S0 = S0 + amt_neg
    return 'supply_0', S0


def update_Q1(params, substep, state_history, prev_state, policy_input):
    # action = _input['action']
    Q1 = prev_state['attestations_1']
    dQ1 = policy_input['action']['amt_Q1']

    Q1 = Q1 + dQ1
    return 'attestations_1', Q1


def update_Q0(params, substep, state_history, prev_state, policy_input):
    # action = _input['action']
    Q0 = prev_state['attestations_0']
    dQ0 = policy_input['action']['amt_Q0']

    Q0 = Q0 + dQ0
    return 'attestations_0', Q0


def update_alpha(params, substep, state_history, prev_state, policy_input):
    S = prev_state['supply']
    I = prev_state['invariant_I']
    kappa = prev_state['kappa']
    C = _params['C']

    alpha = spot_alpha(S, I, kappa, C)
    return 'alpha', alpha


def update_kappa(params, substep, state_history, prev_state, policy_input):
    dR = policy_input['action']['amt_reserve']
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    I = prev_state['invariant_I']
    alpha = prev_state['alpha']

    kappa = kappa(dR, R, S, V, I, alpha)
    return 'kappa', kappa


def update_P(params, substep, state_history, prev_state, policy_input):
    P = spot_price()
    return 'price', P


def update_V(params, substep, state_history, prev_state, policy_input):
    R = prev_state['reserve']
    S = prev_state['supply']
    kappa = prev_state['kappa']

    V = invariant_V(R, S, kappa)
    return 'invariant_V', V


'''
    if action['mech'] == 'attest_pos':      
        dQ1, alpha_belief = attest_pos(amt_a, S1, C, I, params['kappa'])
        S1 = S1 + amt_a
        Q1 = Q1 + dQ1
        alpha = spot_alpha(S, I, kappa, C)
        kappa = kappa(dR, R, S, V, I, alpha)
        P = spot_price()
        V = invariant_V(R, S, kappa)
    
    elif action['mech'] == 'attest_neg':       
        dQ0, alpha_belief = attest_neg(amt_a, S0, C, I, params['kappa'])
        S0 = S0 + amt_a
        Q0 = Q0 + dQ0
        alpha = spot_alpha(S, I, kappa, C)
        kappa = kappa(dR, R, S, V, I, alpha)
        P = spot_price()
        invariant_V(R, S, kappa)
'''
