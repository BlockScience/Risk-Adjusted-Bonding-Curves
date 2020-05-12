from action import *

def update_kappa(params, step, sL, s, _input):

# if action['mech'] == 'attest_pos' or action['mech'] == 'attest_neg'
# elif if action['mech'] == 'bond' or action['mech'] == 'burn'

    action = _input['action']
    kappa = action['posterior']['kappa']
    
    key = 'spot_kappa'
    value = kappa
    
    return (key, value)