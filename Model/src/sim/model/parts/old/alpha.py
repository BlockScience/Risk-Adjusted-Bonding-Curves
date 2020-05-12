from action import *

def update_P(params, step, sL, s, _input):
    
    action = _input['action']
    P = action['posterior']['alpha']
    
    key = 'spot_alpha'
    value = alpha
    
    return (key, value)