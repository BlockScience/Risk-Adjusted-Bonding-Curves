from action import *

# current_state (called s in documentation) is a dict. Captures the current state of the system

P0 = [1]

signal = {
'dP' : ['N/A', P0/4, P0/1000, P0/2],
'period': ['N/A', 2000, 2000, 2000]
}


def update_private_price(_params, substep, state_history, current_state, _input):     
    # Private price belief signal is a sine wave
    new_private_price = P0 + signal['dP']*np.sin(2*np.pi*current_state['timestep']/period)
    return new_private_price



def update_private_alpha(_params, substep, state_history, current_state, _input):    
    # Private alpha belief signal is a ramp   
    sign = (-1)**int((2*current_state['timestep']/period))
    new_private_alpha = current_state['alpha'] + signal['dP']*sign
    return new_private_alpha
