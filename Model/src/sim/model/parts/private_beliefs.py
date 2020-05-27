# from .choose_action import *

# prev_state (called s in documentation) is a dict. Captures the current state of the system
import numpy as np
import matplotlib.pyplot as plt

P0 = [1]

signal = {
    # 'dP': ['N/A', P0[0]/4, P0[0]/1000, P0[0]/2],
    # 'period': ['N/A', 2000, 2000, 2000]
    'dP': P0[0]/4,
    'period': 2000
}


def update_private_price(params, substep, state_history, prev_state, policy_input):
    # Private price belief signal is a sine wave
    print("signal['dP'] = ", signal['dP'])
    print("prev_state['timestep'] = ", prev_state['timestep'])
    new_private_price = P0[0] + signal['dP'] * \
        np.sin(2*np.pi*prev_state['timestep']/signal['period'])
    return 'private_price', new_private_price


def update_private_alpha(params, substep, state_history, prev_state, policy_input):
    # Private alpha belief signal is a ramp
    # sign = (-1)**int((2*prev_state['timestep']/signal['period']))
    # new_private_alpha = prev_state['alpha'] + signal['dP']*sign
    new_private_alpha = P0[0] + signal['dP'] * \
        np.sin(2*np.pi*prev_state['timestep']/signal['period'])
    # plt.plot(new_private_alpha, substep)
    # plt.show()
    print("new_private_alpha = ", new_private_alpha)
    return 'private_alpha', new_private_alpha
