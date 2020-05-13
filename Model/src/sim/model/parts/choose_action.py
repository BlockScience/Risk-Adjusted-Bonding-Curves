# TODO: imports

from .private_beliefs import *


def set_action(params, substep, state_history, prev_state):

    R = prev_state['reserve']
    S = prev_state['supply']
    V = prev_state['invariant_V']
    I = prev_state['invariant_I']
    P = prev_state['spot_price'][substep-2]
    print("SPOT PRICE P =", P)
    print("SUBSTEP =", substep)
    private_price = prev_state['private_price']
    print("private_price =", private_price)
    private_alpha = prev_state['private_alpha']
    print("private_alpha =", private_alpha)
    S1 = prev_state['supply_1']
    S0 = prev_state['supply_0']
    Q1 = prev_state['attestations_1']
    Q0 = prev_state['attestations_0']
    start_kappa = params['starting_kappa']
    start_alpha = params['starting_alpha']
    alpha = prev_state['spot_alpha']
    print("alpha = ", alpha)
    kappa = prev_state['kappa']
    period = params['period']

    # new_private_price is obtained from update_private_price() function in private_beliefs
    if P > private_price:
        mech = 'burn'
        amt_reserve = 0
        amt_supply = P - private_price

    elif P < private_price:
        mech = 'bond'
        amt_reserve = priavte_price - P
        amt_supply = 0

    else:
        # don't trade
        print("No trade")

    if alpha > private_alpha:
        mech = 'attest_neg'
        amt_Q1 = 0
        amt_Q0 = alpha - private_alpha
        amt_neg = amt_Q0  # VERIFY THIS
        amt_pos = 0
        S0 = S0 + amt_neg
        Q0 = Q0 + amt_Q0

    elif alpha < private_alpha:
        mech = 'attest_pos'
        amt_Q1 = private_alpha - alpha
        amt_Q0 = 0
        amt_neg = 0
        amt_pos = amt_Q1  # VERIFY THIS
        S1 = S1 + amt_pos
        Q1 = Q1 + amt_Q1

    else:
        # don't attest
        amt_Q1 = 0
        amt_Q0 = 0
        amt_pos = 0
        amt_neg = 0
        print("No attestation")

        # action['posterior'] = {'S': S, 'R': R, 'P': P, 'S1': S0, 'S1': S1,
        #               'Q0': Q0, 'Q1': Q1, 'kappa': kappa, 'alpha': alpha, 'I': I, 'V': V}

    return {
        'mech': mech,
        'amt_reserve': amt_reserve,
        'amt_supply': amt_supply,
        'amt_Q1': amt_Q1,
        'amt_Q0': amt_Q0,
        'amt_pos': amt_pos,
        'amt_neg': amt_neg,
        # 'p_in': new_price,
        # 'price_belief': price_belief(amt_b),
        # 'alpha_in': new_alpha,
        # 'alpha_belief': alpha_belief(amt_a),
        # 'posterior': {}
    }


"""     action = {
        'mech': mech,
        'amt_reserve': amt_reserve,
        'amt_supply': amt_supply,
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
