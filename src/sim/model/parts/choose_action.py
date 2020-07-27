# TODO: imports
import random
import math
# f = 0.03  # param to control certainty of alpha at extremes
# m = 0.15  # param to modulate curvature of alpha threshold band


def set_action(params, substep, state_history, prev_state):
    # params = params[0]
    # pprint(params)
    #print('Choose Action')
    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    I = prev_state['invariant_I']
    P = prev_state['spot_price']
    private_price = prev_state['chosen_agent']['agent_private_price']
    private_alpha = prev_state['chosen_agent']['agent_private_alpha']
    S1 = prev_state['supply_1']
    S0 = prev_state['supply_0']
    r = prev_state['chosen_agent']['agent_reserve']
    #print("AGENT RESERVE = ", r)
    # s = prev_state['chosen_agent']['agent_supply']
    # this model contains only the notion of s_free. Agent supply is implicit
    s_free = prev_state['chosen_agent']['agent_supply_free']
    """
    r = prev_state['agent_reserve']
    s = prev_state['agent_supply']
    s_free = prev_state['agent_supply_free']
    """
    Q1 = prev_state['attestations_1']
    Q0 = prev_state['attestations_0']
    start_kappa = params['starting_kappa']
    start_alpha = params['starting_alpha']
    alpha = prev_state['alpha']
    kappa = prev_state['kappa']
    f = params['f']
    m = params['m']
    dust = params['dust']
    period = params['period']

    print('r', r)

    # print('P', P, type(P))
    # print('R', R, type(R))
    # print('private_price', private_price, type(private_price))
    # print('s_free', s_free, type(s_free))
    # print('private_alpha', private_alpha, type(private_alpha))
    # print('alpha', alpha, type(alpha))
    # new_private_price is obtained from update_private_price() function in private_beliefs

    # USING ARMIJO RULE
    if P > private_price and s_free > 0 and R > 0:
        mech_bc = 'burn'

        amt_to_bond = 0
        amt_to_burn = s_free*(1-dust)
        print("Agent burns. Amt to burn = ", amt_to_burn)

    elif P < private_price and r > 0 and S > 0:
        mech_bc = 'bond'

        amt_to_bond = r*(1-dust)
        amt_to_burn = 0
        print("Agent bonds. Amt to bond = ", amt_to_bond)

    elif s_free <= 0:
        mech_bc = None
        amt_to_bond = 0
        amt_to_burn = 0
        print("Agent supply too low. No bond/burn", "| s_free = ", s_free)

    elif r <= 0:
        mech_bc = None
        amt_to_bond = 0
        amt_to_burn = 0
        print("Agent reserve too low. No bond/burn", "| r = ", r)

    elif S <= 0:
        mech_bc = None
        amt_to_bond = 0
        amt_to_burn = 0
        print("System supply too low. No bond/burn", "| S = ", S)

    elif R <= 0:
        mech_bc = None
        amt_to_bond = 0
        amt_to_burn = 0
        print("System reserve too low. No bond/burn", "| R = ", R)

    else:
        # don't trade
        mech_bc = None
        amt_to_bond = 0
        amt_to_burn = 0
        print("No trade. P = ", P, "private_price = ", private_price)

    if alpha > private_alpha and s_free > 0:
        mech_pm = 'attest_neg'
        print("Negative attestation. | alpha = ",
              alpha, "private_alpha = ", private_alpha)

        # Agent's choice of delta s
        amt_pos = 0

        # Heuristic 1: Random choice between 0-50% of agent supply
        # amt_neg = (random.randint(0, 50)/100)*s_free

        # Heuristic 2: Variable bandwidth threshold on alpha - private_alpha
        a = abs(alpha - private_alpha)
        d = 4*m*(1-a)*(a)
        g1 = d + (1-d-f)*a + f
        g0 = (1-d-f)*a
        amt_neg = random.uniform(g0, g1)*s_free
        print("amt_neg = ", amt_neg)

        # Compute number of claims
        A = math.sqrt(1+((amt_pos+amt_neg)/S))
        amt_Q1 = 0
        amt_Q0 = Q0*(A-1)
        print("amt_Q0 = ", amt_Q0)

        # amt_Q0 = alpha - private_alpha  # units
        # amt_neg = amt_Q0  # delta_s to S0
        # amt_pos = 0 # delta_s to S1
        # S0 = S0 + amt_neg
        # Q0 = Q0 + amt_Q0

    elif alpha < private_alpha and s_free > 0:
        mech_pm = 'attest_pos'
        print("Positive attestation. | alpha = ",
              alpha, "private_alpha = ", private_alpha)

        # Agent's choice of delta s
        # Heuristic 1: Random choice between 0-50% of agent supply
        # amt_pos = (random.randint(0, 50)/100)*s_free

        # Heuristic 2: Variable bandwidth threshold on alpha - private_alpha
        a = abs(alpha - private_alpha)
        d = 4*m*(1-a)*(a)
        g1 = d + (1-d-f)*a + f
        g0 = (1-d-f)*a
        amt_pos = random.uniform(g0, g1)*s_free

        amt_neg = 0
       # print("amt_pos = ", amt_pos)

        # Compute number of claims
        A = math.sqrt(1+((amt_pos+amt_neg)/S))
        amt_Q1 = Q0*(A-1)
        amt_Q0 = 0
        print("amt_Q1 = ", amt_Q1)

        # amt_Q1 = private_alpha - alpha  # units
        # amt_Q0 = 0
        # amt_neg = 0 # delta_s to S0
        # amt_pos = amt_Q1 # delta_s to S1
        # S1 = S1 + amt_pos
        # Q1 = Q1 + amt_Q1

    elif s_free <= 0:
        mech_pm = 'None'
        amt_pos = 0
        amt_neg = 0
        amt_Q1 = 0
        amt_Q0 = 0
        print("Agent supply too low. Cannot attest")

    else:
        # don't attest
        mech_pm = None
        amt_Q1 = 0
        amt_Q0 = 0
        amt_pos = 0
        amt_neg = 0
        print("No attestation. alpha = ", alpha,
              "private_alpha = ", private_alpha, "s_free = ", s_free)

        # action['posterior'] = {'S': S, 'R': R, 'P': P, 'S1': S0, 'S1': S1,
        #               'Q0': Q0, 'Q1': Q1, 'kappa': kappa, 'alpha': alpha, 'I': I, 'V': V}

    return {
        'mech_bc': mech_bc,
        'mech_pm': mech_pm,
        'amt_to_bond': amt_to_bond,
        'amt_to_burn': amt_to_burn,
        'amt_Q1': amt_Q1,
        'amt_Q0': amt_Q0,
        'amt_pos': amt_pos,
        'amt_neg': amt_neg
        # 'p_in': new_price,
        # 'price_belief': price_belief(amt_b),
        # 'alpha_in': new_alpha,
        # 'alpha_belief': alpha_belief(amt_a),
        # 'posterior': {}
    }


"""     action = {
        'mech': mech,
        'amt_to_bond': amt_to_bond,
        'amt_to_burn': amt_to_burn,
        'amt_Q1': amt_Q1,
        'amt_Q0': amt_Q0,
        'amt_pos': amt_pos,
        'amt_neg': amt_neg,
        # 'p_in': new_price,
        # 'price_belief': price_belief(amt_b),
        # 'alpha_in': new_alpha,
        # 'alpha_belief': alpha_belief(amt_a),
        'posterior': {}
    } """

'''

    if action['mech'] == 'bond':
        dS, price_belief = bond(amt_b, R, S, V, params['kappa'])
        R = R + amt_b
        S = S + dS
        I = R + (C*alpha)
        kappa = kappa(deltaR, R, S, V, I, alpha)
        P = spot_price(R, V, kappa)


    elif action['mech'] == 'burn':
        dR, price_belief = withdraw(amt_b, R, S, V, params['kappa'])
        R = R - dR
        S = S - amt_b
        I = R + (C*alpha)
        kappa = kappa(dR, R, S, V, I, alpha)
        P = spot_price(R, V, kappa)

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

# new_private_price is obtained from update_private_price() function in private_beliefs
"""  if P > private_price and s_free > 0 and R > 0:
           mech_bc = 'burn'  # burn deltaS to get deltaR.
           # print("Agent burns. P = ", P, "| private_price = ", private_price)
           amt_to_bond = 0
           # amt reqd for next state P = current state price belief
           amt_to_burn = (P - private_price) * 0.5 * s_free

       elif P < private_price and r > 0 and S > 0:
           mech_bc = 'bond'  # bond deltaR to get deltaS
           # print("Agent bonds. P = ", P, "| private_price = ", private_price)
           amt_to_bond = (private_price - P) * 0.5 * r  # units
           amt_to_burn = 0 """
