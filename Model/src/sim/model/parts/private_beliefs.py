# from .choose_action import *

# current_state (called s in documentation) is a dict. Captures the current state of the system
import numpy as np

P0 = [1]

signal = {
    # 'dP': ['N/A', P0[0]/4, P0[0]/1000, P0[0]/2],
    # 'period': ['N/A', 2000, 2000, 2000]
    'dP': P0[0]/4,
    'period': 2000
}


def update_private_price(_params, substep, state_history, current_state, _input):
    # Private price belief signal is a sine wave
    print("signal['dP'] = ", signal['dP'])
    print("current_state['timestep'] = ", current_state['timestep'])
    print("signal['period'] = ", signal['period'])
    new_private_price = P0[0] + signal['dP'] * \
        np.sin(2*np.pi*current_state['timestep']/signal['period'])
    return 'private_price', new_private_price


def update_private_alpha(_params, substep, state_history, current_state, _input):
    # Private alpha belief signal is a ramp
    sign = (-1)**int((2*current_state['timestep']/signal['period']))
    new_private_alpha = current_state['alpha'] + signal['dP']*sign
    return 'private alpha', new_private_alpha
