import random
import math

def set_bond_action(params, substep, state_history, prev_state):
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
    # print("AGENT RESERVE = ", r)
    # s = prev_state['chosen_agent']['agent_supply']
    # this model contains only the notion of s_free. Agent supply is implicit
    s_free = prev_state['chosen_agent']['agent_supply_free']
    Q1 = prev_state['attestations_1']
    Q0 = prev_state['attestations_0']
    start_kappa = params['starting_kappa']
    start_alpha = params['starting_alpha']
    alpha = prev_state['alpha']
    kappa = prev_state['kappa']
    f = params['f']
    m = params['m']
    dust = params['dust']
    beta = params['beta']
    period = params['period']
    tau = 0  # 1.2*private_price

    amt_to_burn = 0
        # amt_to_bond = 0

    mech_bc = 'bond'

    deltaR = r*(1-dust)

    amt_to_bond = deltaR
    amt_to_burn = 0

    mech_pm = None
    amt_Q1 = 0
    amt_Q0 = 0
    amt_pos = 0
    amt_neg = 0

    return {
        'mech_bc': mech_bc,
        'mech_pm': mech_pm,
        'amt_to_bond': amt_to_bond,
        'amt_to_burn': amt_to_burn,
        'amt_Q1': amt_Q1,
        'amt_Q0': amt_Q0,
        'amt_pos': amt_pos,
        'amt_neg': amt_neg
    }


def set_action(params, substep, state_history, prev_state):
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
    # print("AGENT RESERVE = ", r)
    # s = prev_state['chosen_agent']['agent_supply']
    # this model contains only the notion of s_free. Agent supply is implicit
    s_free = prev_state['chosen_agent']['agent_supply_free']
    Q1 = prev_state['attestations_1']
    Q0 = prev_state['attestations_0']
    start_kappa = params['starting_kappa']
    start_alpha = params['starting_alpha']
    alpha = prev_state['alpha']
    kappa = prev_state['kappa']
    f = params['f']
    m = params['m']
    dust = params['dust']
    beta = params['beta']
    period = params['period']
    tau = 0  # 1.2*private_price

   # USING ARMIJO RULE
    if P > (private_price + tau) and s_free > 0 and R > 0:
        mech_bc = 'burn'


        deltaS = s_free*(1-dust)
        deltaR = R-((S-deltaS)**kappa)/V
# 
        if deltaS == 0:
            protoRP = kappa*R**((kappa-1)/kappa)/V**(1/kappa)
        else:
            protoRP = deltaR/deltaS
# 
        while protoRP < private_price:
            deltaS = beta*deltaS
# 
            if deltaS == 0:
                protoRP = kappa*R**((kappa-1)/kappa)/V**(1/kappa)
            else:
                protoRP = deltaR/deltaS
            
            if protoRP < dust:
                break
# 
        RP = protoRP
        amt_to_burn = deltaS
        amt_to_bond = 0


    elif P < (private_price - tau) and r > 0 and S > 0:
        mech_bc = 'bond'

        deltaR = r*(1-dust)
        deltaS = (V*(R+deltaR))**(1/kappa)-S
# 
        if deltaS == 0:
            protoRP = kappa*R**((kappa-1)/kappa)/V**(1/kappa)
        else:
            protoRP = deltaR/deltaS
# 
        while protoRP > private_price:
            deltaR = beta*deltaR
# 
            if deltaS == 0:
                protoRP = kappa*R**((kappa-1)/kappa)/V**(1/kappa)
            else:
                protoRP = deltaR/deltaS
            
            if protoRP < dust:
                break
# 
        RP = protoRP
        #print("PROTO RP (BOND) = ", protoRP)
        amt_to_bond = deltaR
        amt_to_burn = 0


    else:
        # don't trade
        mech_bc = None
        amt_to_bond = 0
        amt_to_burn = 0

    if alpha > private_alpha and s_free > 0:
        mech_pm = 'attest_neg'

        # Agent's choice of delta s
        amt_pos = 0


        # Heuristic 2: Variable bandwidth threshold on alpha - private_alpha
        a = abs(alpha - private_alpha)
        d = 4*m*(1-a)*(a)
        g1 = d + (1-d-f)*a + f
        g0 = (1-d-f)*a
        amt_neg = random.uniform(g0, g1)*s_free
        # print("amt_neg = ", amt_neg)

        # Compute number of claims
        A = math.sqrt(1+((amt_pos+amt_neg)/S))
        amt_Q1 = 0
        amt_Q0 = Q0*(A-1)


    elif alpha < private_alpha and s_free > 0:
        mech_pm = 'attest_pos'


        # Heuristic 2: Variable bandwidth threshold on alpha - private_alpha
        a = abs(alpha - private_alpha)
        d = 4*m*(1-a)*(a)
        g1 = d + (1-d-f)*a + f
        g0 = (1-d-f)*a
        amt_pos = random.uniform(g0, g1)*s_free

        amt_neg = 0

        # Compute number of claims
        A = math.sqrt(1+((amt_pos+amt_neg)/S))
        amt_Q1 = Q1*(A-1)
        amt_Q0 = 0

    elif s_free <= 0:
        mech_pm = 'None'
        amt_pos = 0
        amt_neg = 0
        amt_Q1 = 0
        amt_Q0 = 0

    else:
        # don't attest
        mech_pm = None
        amt_Q1 = 0
        amt_Q0 = 0
        amt_pos = 0
        amt_neg = 0


    return {
        'mech_bc': mech_bc,
        'mech_pm': mech_pm,
        'amt_to_bond': amt_to_bond,
        'amt_to_burn': amt_to_burn,
        'amt_Q1': amt_Q1,
        'amt_Q0': amt_Q0,
        'amt_pos': amt_pos,
        'amt_neg': amt_neg
    }


