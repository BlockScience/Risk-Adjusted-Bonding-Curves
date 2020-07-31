# from Model.src.sim.model.parts.choose_action import *

# prev_state (called s in documentation) is a dict. Captures the current state of the system
import numpy as np
import random
import matplotlib.pyplot as plt

# REMOVE and put in update_private_price function
# Should be part of parameter if will be varied

# P0 = [1]

# signal = {
#     # 'dP': ['N/A', P0[0]/4, P0[0]/1000, P0[0]/2],
#     # 'period': ['N/A', 2000, 2000, 2000]
#     'dP': P0[0]/4,
#     'period': 2000,
#     'sigma': [.005, 'N/A', 'N/A', 'N/A']
# }


def update_private_price(params, substep, state_history, prev_state, policy_input):

    P0 = 1

    signal = {
        # 'dP': ['N/A', P0[0]/4, P0[0]/1000, P0[0]/2],
        # 'period': ['N/A', 2000, 2000, 2000]
        'P0': P0,
        'dP': P0/4,
        'period': 2000,
        'sigma': .005  # , 'N/A', 'N/A', 'N/A']
    }

    print("UPDATE PRIVATE PRICE")
    #params = params[0]
    rules_price = params['rules_price']
    period = params['period']
    timestep = prev_state['timestep']
    price = prev_state['spot_price']

    """ if rules_price == 'step':
        bump = int((timestep % int(period/2) == 0))*int(timestep > 0)
        sign = -(-1)**int((2*timestep/period))
        new_private_price = price + signal['dP']*bump*sign
    elif rules_price == 'ramp':
        sign = (-1)**int((2*timestep/period))
        new_private_price = price + signal['dP']*sign
    elif rules_price == 'sin':
        new_private_price = P0 + signal['dP'] * \
            np.sin(2*np.pi*timestep/period)
    elif rules_price == 'martin':
        rv = np.random.normal(0, signal['sigma'])
        new_private_price = price+price*rv
    else:
        new_private_price = price """

    # Private price belief signal is a sine wave
    # print("signal['dP'] = ", signal['dP'])
    # print("prev_state['timestep'] = ", prev_state['timestep'])

    #new_private_price = (random.randint(0, 100))/100

    # new_private_price = P0[0] + signal['dP'] * \
    #    np.sin(2*np.pi*prev_state['timestep']/signal['period'])

    # use martingale

    # Private price is a noisy reserve/supply <-- not using
    #r = prev_state['reserve']
    #s = prev_state['supply']
    #noise_r = (random.randint(-50, 50)/100)
    #noise_s = (random.randint(-50, 50)/100)

    #print("noise r = ", noise_r)
    #print("noise s = ", noise_s)

    #new_private_price = (r + (noise_r * r)) / (s + (noise_s * s))
    print("--------------------------------------")

    new_private_price = prev_state['chosen_agent']['agent_private_price']

    return 'private_price', new_private_price


def update_private_alpha(params, substep, state_history, prev_state, policy_input):
    # Private alpha belief signal is a ramp
    #sign = (-1)**int((2*prev_state['timestep']/signal['period']))
    #new_private_alpha = prev_state['alpha'] + signal['dP']*sign

    # new_private_alpha = P0[0] + signal['dP'] * \
    #  np.sin(2*np.pi*prev_state['timestep']/signal['period'])

    # new_private_alpha = (random.randint(50, 100))/100

    new_private_alpha = prev_state['chosen_agent']['agent_private_alpha']

    # print("new_private_alpha = ", new_private_alpha)
    return 'private_alpha', new_private_alpha


def update_agent_beliefs(params, substep, state_history, prev_state, policy_input):

    agent = prev_state['chosen_agent']

    new_private_price = agent['agent_private_price']
    new_private_alpha = agent['agent_private_alpha']

    agent['agent_private_price'] = new_private_price
    agent['agent_private_alpha'] = new_private_alpha

    print("agent['agent_private_price'] = ", agent['agent_private_price'])
    print("agent['agent_private_alpha'] = ", agent['agent_private_alpha'])

    return 'chosen_agent', agent
