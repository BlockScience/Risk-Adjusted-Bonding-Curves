from action import *

# Include this function as another part so as to account for all mechansims (?)
# don't require this because handling with amounts (0 vs +ve) instead of action performed
'''def action_taken():
    action = _input['action']
    if action['mech'] == 'attest_pos':
        S1 = current_state['supply_1']
        dQ1, alpha_belief = attest_pos(amt_pos, S1, C, I, params['kappa'])
    elif action['mech'] == 'attest_neg':       
        dQ0, alpha_belief = attest_neg(amt_neg, S0, C, I, params['kappa'])
    return #?????? ''''
        
def update_S1(_params, substep, state_history, current_state, _input):
    #action = _input['action']
    S1 = current_state['supply_1']
    # amt_pos is a key in a dict of dicts 
    amt_pos = _input['action']['amt_pos']
    
    S1 = S1 + amt_pos
    return 'supply_1', S1
    
def update_S0(_params, substep, state_history, current_state, _input):
    S0 = current_state['supply_0']
    amt_neg = _input['action']['amt_neg']
     
    S0 = S0 + amt_neg
    return 'supply_0', S0
    
    
def update_Q1(_params, substep, state_history, current_state, _input):
    # action = _input['action']
    Q1 = current_state['attestations_1']
    dQ1 = _input['action']['amt_Q1']
    
    Q1 = Q1 + dQ1
    return 'attestations_1', Q1

    
def update_Q0(_params, substep, state_history, current_state, _input):
    # action = _input['action']    
    Q0 = current_state['attestations_0']
    dQ0 = _input['action']['amt_Q0']
        
    Q0 = Q0 + dQ0
    return 'attestations_0', Q0
    
def update_alpha(_params, substep, state_history, current_state, _input):
    S = current_state['supply']
    I = current_state['invariant_I'] 
    kappa = current_state['kappa'] 
    C = _params['C']
    
    alpha = spot_alpha(S, I, kappa, C)
    return 'alpha', alpha

def update_kappa(_params, substep, state_history, current_state, _input):
    dR = _input['action']['amt_reserve']
    R = current_state['reserve']
    S = current_state['supply']
    V = current_state['invariant_V']
    I = current_state['invariant_I'] 
    alpha = current_state['alpha']
    
    kappa = kappa(dR, R, S, V, I, alpha)
    return 'kappa', kappa

def update_P(_params, substep, state_history, current_state, _input):
    P = spot_price()
    return 'price', P

def update_V(_params, substep, state_history, current_state, _input):
    R = current_state['reserve']
    S = current_state['supply']
    kappa = current_state['kappa']
    
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