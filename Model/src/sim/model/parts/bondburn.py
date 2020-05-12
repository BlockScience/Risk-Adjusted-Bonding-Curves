from action import *

# Include this function as another part so as to account for all mechansims (?)
# don't require this because handling with amounts (0 vs +ve) instead of action performed
'''def action_taken():
    if action['mech'] == 'bond':
        dS, pbar = bond(amt_reserve, R, S, V, params['kappa'])
    elif action['mech'] == 'burn': 
        dR, pbar = withdraw(amt_supply, R, S, V, params['kappa'])
    else:
        print("No bond or burn made")
    return #?????? '''

def update_R(_params, substep, state_history, current_state, _input):
    #action = _input['action']
    #deltaS = _input['amt_supply'] 
    # access amt_supply using _input['action']['amt_supply'] because it's a dict of dicts
    deltaS = _input['action']['amt_supply']
    
    deltaR = R-((S-deltaS)**kappa)/V0
    R = R + _input['action']['amt_reserve'] - deltaR
    print(R)

    return 'reserve', R

def update_S(_params, substep, state_history, current_state, _input):
    #action = _input['action']
    #deltaR = _input['amt_reserve']
    deltaR = _input['action']['amt_reserve']
    
    deltaS = (V0*(R+deltaR))**(1/kappa)-S
    S = S + deltaS - _input['action']['amt_supply']

    return 'supply', S

def update_price(_params, substep, state_history, current_state, _input):
    R = current_state['reserve']
    V = current_state['invariant_V']
    kappa = current_state['kappa']
    
    P = spot_price(R, V, kappa)
    return 'price', P

def update_pbar(_params, substep, state_history, current_state, _input):
    deltaS = _input['action']['amt_supply']
    deltaR = _input['action']['amt_reserve']
    
    if deltaS == 0:   
        deltaS = (V0*(R+deltaR))**(1/kappa)-S        
    elif deltaR == 0:
        deltaR = R-((S-deltaS)**kappa)/V0        
      
    realized_price = deltaR/deltaS
    pbar = realized_price
    return 'realized_price', pbar

def update_I(_params, substep, state_history, current_state, _input):
    R = current_state['reserve']
    C = _params['C']
    alpha = current_state['alpha']
    
    I = R + (C*alpha)
    return 'invariant_I', I

# kappa does not change
#def update_kappa(_params, substep, state_history, current_state, _input):
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