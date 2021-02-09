import numpy as np 

def synthetic_alpha_test(params, substep, state_history, prev_state):

    previous_public_alpha = prev_state['public_alpha']

    alpha_noise = round(np.random.normal(0.1,0.05,1)[0],2) / 15

    if params['alpha_test'] == 'success':
        new_public_alpha = 1 - (1- (alpha_noise)) * (1 - previous_public_alpha)

    elif params['alpha_test'] == 'failure':      
        new_public_alpha = (1- (alpha_noise)) * (previous_public_alpha)
  
    elif params['alpha_test'] == 'constant':      
        new_public_alpha = previous_public_alpha

    delta_public_alpha = new_public_alpha - previous_public_alpha

    return {'public_alpha_update': new_public_alpha, 'delta_public_alpha' : delta_public_alpha}


def delta_public_alpha_update(params, substep, state_history, prev_state, policy_input):
    '''
    Tracks delta public alpha signal, used to generate alpha
    '''
    # previous_alpha = prev_state['public_alpha']
    delta_public_alpha = policy_input['delta_public_alpha']

    return 'delta_public_alpha', delta_public_alpha

def public_alpha_update(params, substep, state_history, prev_state, policy_input):
    '''
    Tracks public alpha signal, used to generate alpha
    '''
    # previous_alpha = prev_state['public_alpha']
    new_alpha = policy_input['public_alpha_update']

    return 'public_alpha', new_alpha