import random
# E = 0.2
# Remove update_Q (?) since total number of attestations Q = Q1 + Q0


def update_Q(params, substep, state_history, prev_state, policy_input):
    Q = prev_state['attestations']
    dQ = policy_input['amt_Q1'] + policy_input['amt_Q0']

    Q = Q + dQ
    return 'attestations', Q


def update_Q1(params, substep, state_history, prev_state, policy_input):
    Q1 = prev_state['attestations_1']

    Q1 = Q1 + policy_input['amt_Q1']
    return 'attestations_1', Q1


def update_Q0(params, substep, state_history, prev_state, policy_input):
    Q0 = prev_state['attestations_0']

    Q0 = Q0 + policy_input['amt_Q0']
    return 'attestations_0', Q0


def update_S1(params, substep, state_history, prev_state, policy_input):
    # action = _input['action']
    S1 = prev_state['supply_1']
    # amt_pos is a key in a dict of dicts

    S1 = S1 + policy_input['amt_pos']
    return 'supply_1', S1


def update_S0(params, substep, state_history, prev_state, policy_input):
    S0 = prev_state['supply_0']

    S0 = S0 + policy_input['amt_neg']
    return 'supply_0', S0


def update_S_free(params, substep, state_history, prev_state, policy_input):
    S_free = prev_state['supply_free']

    S_free = S_free - (policy_input['amt_neg'] + policy_input['amt_pos'])
    return 'supply_free', S_free


def compute_q1(q1, amt_Q1):

    q1 = q1 + amt_Q1

    #print("amt_Q1 from compute_q1: ", amt_Q1)

    return q1


def compute_q0(q0, amt_Q0):

    q0 = q0 + amt_Q0

    return q0


def compute_s1(s1, amt_pos):

    s1 = s1 + amt_pos

    return s1


def compute_s0(s0, amt_neg):

    s0 = s0 + amt_neg

    return s0


def compute_s_free(s_free, delta_s_free):

    s_free = s_free - delta_s_free

    return s_free


def update_agent_PM(params, substep, state_history, prev_state, policy_input):
    agent = prev_state['chosen_agent']
    q1 = agent['agent_attestations_1']
    q0 = agent['agent_attestations_0']
    s1 = agent['agent_supply_1']
    s0 = agent['agent_supply_0']
    s_free = agent['agent_supply_free']

    amt_Q1 = policy_input['amt_Q1']
    amt_Q0 = policy_input['amt_Q0']
    amt_pos = policy_input['amt_pos']
    amt_neg = policy_input['amt_neg']
    delta_s_free = policy_input['amt_pos'] + policy_input['amt_neg']

    #print("amt_Q1 from update_agent: ", amt_Q1)

    agent['agent_attestations_1'] = compute_q1(q1, amt_Q1)
    agent['agent_attestations_0'] = compute_q0(q0, amt_Q0)
    agent['agent_supply_1'] = compute_s1(s1, amt_pos)
    agent['agent_supply_0'] = compute_s0(s0, amt_neg)
    agent['agent_supply_free'] = compute_s_free(s_free, delta_s_free)

    return 'chosen_agent', agent


""" def update_q1(params, substep, state_history, prev_state, policy_input):
    ### was agents_df #########################
    # shoud be agents
    # either the state agent_attestations_1
    # OR state agent_df with choosing series

    agent = prev_state['chosen_agent']

    print('q1 before' + agent.to_string())

    q1 = agent['q1']
    q1 = q1 + policy_input['amt_Q1']
    agent['q1'] = q1

    print('q1 after' + agent.to_string())

    return 'chosen_agent', agent


def update_q0(params, substep, state_history, prev_state, policy_input):
    agent = prev_state['chosen_agent']
    print('q0 before' + agent.to_string())

    q0 = calculate_q0(agent q0, )
    agent['q0']
    q0 = q0 + policy_input['amt_Q0']
    agent['q0'] = q0

    print('q0 after' + agent.to_string())

    return 'chosen_agent', agent


def update_s_free(params, substep, state_history, prev_state, policy_input):
    s_free = prev_state['agent_supply_free']
    delta_s_free = policy_input['amt_pos'] + policy_input['amt_neg']

    print("------timestep-----", prev_state['timestep'] % 50)
    if prev_state['timestep'] % 50 == 0:
        random_drop = 10
    else:
        random_drop = 0

    print("------RANDOM DROP------", random_drop)
    s_free = s_free - delta_s_free + random_drop
    print("-----s_free-----", s_free)
    return 'agent_supply_free', s_free


def update_s1(params, substep, state_history, prev_state, policy_input):
    s1 = prev_state['agent_supply_1']

    s1 = s1 + policy_input['amt_pos']
    return 'agent_supply_1', s1


def update_s0(params, substep, state_history, prev_state, policy_input):
    s0 = prev_state['agent_supply_0']

    s0 = s0 + policy_input['amt_neg']
    return 'agent_supply_0', s0
 """

def attest_pos(R, C, E, alpha, Q, Q1, Q0, S, S1, S0, q0, q1, s_free, s1, s0, s, delta_q1, delta_q0, delta_s ):

    print("Positive attestation")
    new_alpha = S1* R / ( S1* R - S0 * R + S0*C) 

    return new_alpha

def attest_neg(R, C, E, alpha, Q, Q1, Q0, S, S1, S0, q0, q1, s_free, s1, s0, s, delta_q1, delta_q0, delta_s  ):


    new_alpha = S1* R / ( S1* R - S0 * R + S0*C) 

    print("Negative attestation.")

    return new_alpha

def update_alpha(params, substep, state_history, prev_state, policy_input):

    R = prev_state['reserve']
    C = params['C']
    E = params['E']
    alpha = prev_state['alpha']

    Q = prev_state['attestations_1'] + prev_state['attestations_0']
    Q1 = prev_state['attestations_1']
    Q0 = prev_state['attestations_0']
    S = prev_state['supply']
    S1 = prev_state['supply_1']
    S0 = prev_state['supply_0']

    q1 = prev_state['chosen_agent']['agent_attestations_1']
    q0 = prev_state['chosen_agent']['agent_attestations_0']
    s_free = prev_state['chosen_agent']['agent_supply_free']
    s1 = prev_state['chosen_agent']['agent_supply_1']
    s0 = prev_state['chosen_agent']['agent_supply_0']

    s = s_free + s1 + s0

    attest_action = policy_input['mech_pm']
    delta_q1 = policy_input['amt_Q1']
    delta_q0 = policy_input['amt_Q0']
    delta_s = policy_input['amt_pos'] + policy_input['amt_neg']

    if attest_action == 'attest_pos':  # positive attestation
        new_alpha = attest_pos(R, C, E, alpha, Q, Q1, Q0, S, S1, S0, q0, q1, s_free, s1, s0, s, delta_q1, delta_q0, delta_s )
        print("Positive attestation")

    elif attest_action == 'attest_neg':  # negative attestation
        new_alpha = attest_neg(R, C, E, alpha, Q, Q1, Q0, S, S1, S0, q0, q1, s_free, s1, s0, s, delta_q1, delta_q0, delta_s )
        print("Negative attestation.")

    else:
        new_alpha = alpha

    # alpha = spot_alpha(S, I, kappa, C)
    print("Q0 = ", prev_state['attestations_0'], "| Q1 = ", prev_state['attestations_1'],
          "| q0 = ", prev_state['chosen_agent']['agent_attestations_0'], "| q1 = ", prev_state['chosen_agent']['agent_attestations_1'])
    print("deltaq0 = ", delta_q0, "deltaq1 = ", delta_q1)
    print("s = ", s, "| delta_s = ", delta_s)
    # print("A = ", A)
    # print("alpha_bar = ", alpha_bar)
    #print("new_alpha = ", new_alpha)
    # new_alpha = -1*new_alpha
    return 'alpha', new_alpha


def update_kappa(params, substep, state_history, prev_state, policy_input):

    R = prev_state['reserve']
    C = params['C']
    E = params['E']

    alpha = prev_state['alpha']

    Q = prev_state['attestations_1'] + prev_state['attestations_0']
    Q1 = prev_state['attestations_1']
    Q0 = prev_state['attestations_0']
    S = prev_state['supply']
    S1 = prev_state['supply_1']
    S0 = prev_state['supply_0']
    I = prev_state['invariant_I']

    q1 = prev_state['chosen_agent']['agent_attestations_1']
    q0 = prev_state['chosen_agent']['agent_attestations_0']
    s_free = prev_state['chosen_agent']['agent_supply_free']
    s1 = prev_state['chosen_agent']['agent_supply_1']
    s0 = prev_state['chosen_agent']['agent_supply_0']

    s = s_free + s1 + s0

    delta_q1 = policy_input['amt_Q1']
    delta_q0 = policy_input['amt_Q0']
    delta_s = policy_input['amt_pos'] + policy_input['amt_neg']

    if delta_q1 > 0:  # positive attestation
        new_alpha = attest_pos(R, C, E, alpha, Q, Q1, Q0, S, S1, S0, q0, q1, s_free, s1, s0, s, delta_q1, delta_q0, delta_s )

    elif delta_q0 > 0:  # negative attestation

        new_alpha = attest_neg(R, C, E, alpha, Q, Q1, Q0, S, S1, S0, q0, q1, s_free, s1, s0, s, delta_q1, delta_q0, delta_s )

    else:
        new_alpha = alpha

#######   REWRITE INVARIANT I, DO NOT UPDATE I for updated kappa (f of updated alpha)
#  Use Note that in HackMD #
    # I = R + (C*new_alpha)
# if not used, price and s_free go very negative at the outset    
########################################################
    kappa = I / (I - (C*new_alpha))

    #print("kappa  = ", kappa)
    return 'kappa', kappa


def update_I_attest(params, substep, state_history, prev_state, policy_input):
    R = prev_state['reserve']
    C = params['C']
    E = params['E']

    alpha = prev_state['alpha']

    Q = prev_state['attestations_1'] + prev_state['attestations_0']
    Q1 = prev_state['attestations_1']
    Q0 = prev_state['attestations_0']
    S = prev_state['supply']
    S1 = prev_state['supply_1']
    S0 = prev_state['supply_0']

    q1 = prev_state['chosen_agent']['agent_attestations_1']
    q0 = prev_state['chosen_agent']['agent_attestations_0']
    s_free = prev_state['chosen_agent']['agent_supply_free']
    s1 = prev_state['chosen_agent']['agent_supply_1']
    s0 = prev_state['chosen_agent']['agent_supply_0']

    s = s_free + s1 + s0

    delta_q1 = policy_input['amt_Q1']
    delta_q0 = policy_input['amt_Q0']
    delta_s = policy_input['amt_pos'] + policy_input['amt_neg']

    if delta_q1 > 0:  # positive attestation
        new_alpha = attest_pos(R, C, E, alpha, Q, Q1, Q0, S, S1, S0, q0, q1, s_free, s1, s0, s, delta_q1, delta_q0, delta_s )

    elif delta_q0 > 0:  # negative attestation

        new_alpha = attest_neg(R, C, E, alpha, Q, Q1, Q0, S, S1, S0, q0, q1, s_free, s1, s0, s, delta_q1, delta_q0, delta_s )

    else:
        new_alpha = alpha

    I = R + (C*new_alpha)

    #print("I (attest) = ", I)
    return "invariant_I", I


def update_P_attest(params, substep, state_history, prev_state, policy_input):

    R = prev_state['reserve']
    C = params['C']
    E = params['E']
    I = prev_state['invariant_I']
    alpha = prev_state['alpha']

    Q = prev_state['attestations_1'] + prev_state['attestations_0']
    Q1 = prev_state['attestations_1']
    Q0 = prev_state['attestations_0']
    S = prev_state['supply']
    S1 = prev_state['supply_1']
    S0 = prev_state['supply_0']

    q1 = prev_state['chosen_agent']['agent_attestations_1']
    q0 = prev_state['chosen_agent']['agent_attestations_0']
    s_free = prev_state['chosen_agent']['agent_supply_free']
    s1 = prev_state['chosen_agent']['agent_supply_1']
    s0 = prev_state['chosen_agent']['agent_supply_0']

    s = s_free + s1 + s0

    delta_q1 = policy_input['amt_Q1']
    delta_q0 = policy_input['amt_Q0']
    delta_s = policy_input['amt_pos'] + policy_input['amt_neg']

    if delta_q1 > 0:  # positive attestation
        new_alpha = attest_pos(R, C, E, alpha, Q, Q1, Q0, S, S1, S0, q0, q1, s_free, s1, s0, s, delta_q1, delta_q0, delta_s )

    elif delta_q0 > 0:  # negative attestation

        new_alpha = attest_neg(R, C, E, alpha, Q, Q1, Q0, S, S1, S0, q0, q1, s_free, s1, s0, s, delta_q1, delta_q0, delta_s )
    else:
        new_alpha = alpha

    # I = R + (C*new_alpha)
    kappa = I / (I - (C*new_alpha))

    P = kappa * (R/S)

    # VERIFY how this is different from dR/dS and their applicability
    # P = kappa*(R/S)
    #print("Spot Price P (attest) = ", P)
    return 'spot_price', P


def update_V(params, substep, state_history, prev_state, policy_input):

    R = prev_state['reserve']
    C = params['C']
    E = params['E']
    I = prev_state['invariant_I']
    alpha = prev_state['alpha']

    Q = prev_state['attestations_1'] + prev_state['attestations_0']
    Q1 = prev_state['attestations_1']
    Q0 = prev_state['attestations_0']
    S = prev_state['supply']
    S1 = prev_state['supply_1']
    S0 = prev_state['supply_0']

    q1 = prev_state['chosen_agent']['agent_attestations_1']
    q0 = prev_state['chosen_agent']['agent_attestations_0']
    s_free = prev_state['chosen_agent']['agent_supply_free']
    s1 = prev_state['chosen_agent']['agent_supply_1']
    s0 = prev_state['chosen_agent']['agent_supply_0']

    s = s_free + s1 + s0

    delta_q1 = policy_input['amt_Q1']
    delta_q0 = policy_input['amt_Q0']
    delta_s = policy_input['amt_pos'] + policy_input['amt_neg']

    if delta_q1 > 0:  # positive attestation
        new_alpha = attest_pos(R, C, E, alpha, Q, Q1, Q0, S, S1, S0, q0, q1, s_free, s1, s0, s, delta_q1, delta_q0, delta_s )

    elif delta_q0 > 0:  # negative attestation

        new_alpha = attest_neg(R, C, E, alpha, Q, Q1, Q0, S, S1, S0, q0, q1, s_free, s1, s0, s, delta_q1, delta_q0, delta_s )

    else:
        new_alpha = alpha

    # I = R + (C*new_alpha)
    kappa = I / (I - (C*new_alpha))
    V = (S**(kappa))/R

    return 'invariant_V', V

#    R = prev_state['reserve']
#    S = prev_state['supply']
#    kappa = prev_state['kappa']

#    V = invariant_V(R, S, kappa) """
