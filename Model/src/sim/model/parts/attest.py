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
    # action = _input['action']
    S1 = prev_state['supply_1']
    # amt_pos is a key in a dict of dicts
    amt_pos = policy_input['amt_pos']

    S1 = S1 + amt_pos
    return 'supply_1', S1


def update_S0(params, substep, state_history, prev_state, policy_input):
    S0 = prev_state['supply_0']
    amt_neg = policy_input['amt_neg']

    S0 = S0 + amt_neg
    return 'supply_0', S0


def update_Q1(params, substep, state_history, prev_state, policy_input):
    # action = _input['action']
    Q1 = prev_state['attestations_1']
    dQ1 = policy_input['amt_Q1']

    Q1 = Q1 + dQ1
    return 'attestations_1', Q1


def update_Q0(params, substep, state_history, prev_state, policy_input):
    # action = _input['action']
    Q0 = prev_state['attestations_0']
    dQ0 = policy_input['amt_Q0']

    Q0 = Q0 + dQ0
    return 'attestations_0', Q0


def update_alpha(params, substep, state_history, prev_state, policy_input):
    # S = prev_state['supply']
    # I = prev_state['invariant_I']
    # kappa = prev_state['kappa']
    alpha = prev_state['alpha']
    R = prev_state['reserve']
    C = params['C']
    S1 = prev_state['supply_1']
    S0 = prev_state['supply_0']

    deltas = policy_input['amt_pos'] + policy_input['amt_neg']
    deltaq1 = policy_input['amt_Q1']
    deltaq0 = policy_input['amt_Q0']

    if deltaq1 > 0:
        Q1 = prev_state['attestations_1']
        q1 = prev_state['agent_attestations_1']
        s1 = prev_state['agent_supply_1']
        #  deltas = policy_input['amt_pos']
        A = (1/(Q1*(Q1+deltaq1))) * \
            ((q1*(Q1*deltas) - (deltaq1*s)) + deltaq1*((Q1*s1) + (Q1*deltas)))

        alpha_bar = (deltas*R)/(A*(C+R) - (deltas*C))

        new_alpha = E*(alpha) + (1-E)*(alpha)*((S1+S0)/(S1+S0+deltas)) + \
            (alpha_bar)*(deltas/(S1+S0+deltas))

    elif deltaq0 > 0:
        Q0 = prev_state['attestations_0']
        # deltas = policy_input['amt_neg']
        A = (1/(Q0*(Q0+deltaq0))) * \
            ((q0*(Q0*deltas) - (deltaq0*s)) + deltaq0*((Q0*s0) + (Q0*deltas)))

        alpha_bar = (deltas*R)/(A*(C+R) - (deltas*C))

        new_alpha = E*(alpha) + (1-E)*(alpha)*((S1+S0)/(S1+S0+deltas)) + \
            (alpha_bar)*(deltas/(S1+S0+deltas))

    else:
        new_alpha = alpha

    # alpha = spot_alpha(S, I, kappa, C)
    return 'alpha', new_alpha


def update_I(params, substep, state_history, prev_state, policy_input):
    alpha = prev_state['alpha']
    R = prev_state['reserve']
    C = params['C']
    S1 = prev_state['supply_1']
    S0 = prev_state['supply_0']

    deltas = policy_input['amt_pos'] + policy_input['amt_neg']
    deltaq1 = policy_input['amt_Q1']
    deltaq0 = policy_input['amt_Q0']

    if deltaq1 > 0:
        Q1 = prev_state['attestations_1']
        q1 = prev_state['agent_attestations_1']
        s1 = prev_state['agent_supply_1']
        #  deltas = policy_input['amt_pos']
        A = (1/(Q1*(Q1+deltaq1))) * \
            ((q1*(Q1*deltas) - (deltaq1*s)) + deltaq1*((Q1*s1) + (Q1*deltas)))

        alpha_bar = (deltas*R)/(A*(C+R) - (deltas*C))

        new_alpha = E*(alpha) + (1-E)*(alpha)*((S1+S0)/(S1+S0+deltas)) + \
            (alpha_bar)*(deltas/(S1+S0+deltas))

    elif deltaq0 > 0:
        Q0 = prev_state['attestations_0']
        # deltas = policy_input['amt_neg']
        A = (1/(Q0*(Q0+deltaq0))) * \
            ((q0*(Q0*deltas) - (deltaq0*s)) + deltaq0*((Q0*s0) + (Q0*deltas)))

        alpha_bar = (deltas*R)/(A*(C+R) - (deltas*C))

        new_alpha = E*(alpha) + (1-E)*(alpha)*((S1+S0)/(S1+S0+deltas)) + \
            (alpha_bar)*(deltas/(S1+S0+deltas))

    else:
        new_alpha = alpha

    I = R + (C*new_alpha)

    return 'invariant_I', I


def update_kappa(params, substep, state_history, prev_state, policy_input):
    alpha = prev_state['alpha']
    R = prev_state['reserve']
    C = params['C']
    S1 = prev_state['supply_1']
    S0 = prev_state['supply_0']

    deltas = policy_input['amt_pos'] + policy_input['amt_neg']
    deltaq1 = policy_input['amt_Q1']
    deltaq0 = policy_input['amt_Q0']

    if deltaq1 > 0:
        Q1 = prev_state['attestations_1']
        q1 = prev_state['agent_attestations_1']
        s1 = prev_state['agent_supply_1']
        #  deltas = policy_input['amt_pos']
        A = (1/(Q1*(Q1+deltaq1))) * \
            ((q1*(Q1*deltas) - (deltaq1*s)) + deltaq1*((Q1*s1) + (Q1*deltas)))

        alpha_bar = (deltas*R)/(A*(C+R) - (deltas*C))

        new_alpha = E*(alpha) + (1-E)*(alpha)*((S1+S0)/(S1+S0+deltas)) + \
            (alpha_bar)*(deltas/(S1+S0+deltas))

    elif deltaq0 > 0:
        Q0 = prev_state['attestations_0']
        # deltas = policy_input['amt_neg']
        A = (1/(Q0*(Q0+deltaq0))) * \
            ((q0*(Q0*deltas) - (deltaq0*s)) + deltaq0*((Q0*s0) + (Q0*deltas)))

        alpha_bar = (deltas*R)/(A*(C+R) - (deltas*C))

        new_alpha = E*(alpha) + (1-E)*(alpha)*((S1+S0)/(S1+S0+deltas)) + \
            (alpha_bar)*(deltas/(S1+S0+deltas))

    else:
        new_alpha = alpha

    I = R + (C*new_alpha)

    kappa = I / (I - (C*new_alpha))

    # kappa = kappa(dR, R, S, V, I, alpha)
    return 'kappa', kappa


def update_P(params, substep, state_history, prev_state, policy_input):

    alpha = prev_state['alpha']
    R = prev_state['reserve']
    S = prev_state['supply']
    C = params['C']
    S1 = prev_state['supply_1']
    S0 = prev_state['supply_0']

    deltas = policy_input['amt_pos'] + policy_input['amt_neg']
    deltaq1 = policy_input['amt_Q1']
    deltaq0 = policy_input['amt_Q0']

    if deltaq1 > 0:
        Q1 = prev_state['attestations_1']
        q1 = prev_state['agent_attestations_1']
        s1 = prev_state['agent_supply_1']
        #  deltas = policy_input['amt_pos']
        A = (1/(Q1*(Q1+deltaq1))) * \
            ((q1*(Q1*deltas) - (deltaq1*s)) + deltaq1*((Q1*s1) + (Q1*deltas)))

        alpha_bar = (deltas*R)/(A*(C+R) - (deltas*C))

        new_alpha = E*(alpha) + (1-E)*(alpha)*((S1+S0)/(S1+S0+deltas)) + \
            (alpha_bar)*(deltas/(S1+S0+deltas))

    elif deltaq0 > 0:
        Q0 = prev_state['attestations_0']
        # deltas = policy_input['amt_neg']
        A = (1/(Q0*(Q0+deltaq0))) * \
            ((q0*(Q0*deltas) - (deltaq0*s)) + deltaq0*((Q0*s0) + (Q0*deltas)))

        alpha_bar = (deltas*R)/(A*(C+R) - (deltas*C))

        new_alpha = E*(alpha) + (1-E)*(alpha)*((S1+S0)/(S1+S0+deltas)) + \
            (alpha_bar)*(deltas/(S1+S0+deltas))

    else:
        new_alpha = alpha

    I = R + (C*new_alpha)

    kappa = I / (I - (C*new_alpha))

    P = kappa * (R/S)
    # VERIFY how this is different from dR/dS and their applicability
    # P = kappa*(R/S)
    return 'price', P


def update_V(params, substep, state_history, prev_state, policy_input):

    alpha = prev_state['alpha']
    R = prev_state['reserve']
    S = prev_state['supply']
    C = params['C']
    S1 = prev_state['supply_1']
    S0 = prev_state['supply_0']

    deltas = policy_input['amt_pos'] + policy_input['amt_neg']
    deltaq1 = policy_input['amt_Q1']
    deltaq0 = policy_input['amt_Q0']

    if deltaq1 > 0:
        Q1 = prev_state['attestations_1']
        q1 = prev_state['agent_attestations_1']
        s1 = prev_state['agent_supply_1']
        #  deltas = policy_input['amt_pos']
        A = (1/(Q1*(Q1+deltaq1))) * \
            ((q1*(Q1*deltas) - (deltaq1*s)) + deltaq1*((Q1*s1) + (Q1*deltas)))

        alpha_bar = (deltas*R)/(A*(C+R) - (deltas*C))

        new_alpha = E*(alpha) + (1-E)*(alpha)*((S1+S0)/(S1+S0+deltas)) + \
            (alpha_bar)*(deltas/(S1+S0+deltas))

    elif deltaq0 > 0:
        Q0 = prev_state['attestations_0']
        # deltas = policy_input['amt_neg']
        A = (1/(Q0*(Q0+deltaq0))) * \
            ((q0*(Q0*deltas) - (deltaq0*s)) + deltaq0*((Q0*s0) + (Q0*deltas)))

        alpha_bar = (deltas*R)/(A*(C+R) - (deltas*C))

        new_alpha = E*(alpha) + (1-E)*(alpha)*((S1+S0)/(S1+S0+deltas)) + \
            (alpha_bar)*(deltas/(S1+S0+deltas))

    else:
        new_alpha = alpha

    I = R + (C*new_alpha)

    kappa = I / (I - (C*new_alpha))

    V = (S**(kappa))/R

    return 'invariant_V', V

#    R = prev_state['reserve']
#    S = prev_state['supply']
#    kappa = prev_state['kappa']

#    V = invariant_V(R, S, kappa) """


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
