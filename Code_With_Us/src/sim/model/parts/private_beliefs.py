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
    ## params = params[0]
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
    # print("--------------------------------------")

    new_private_price = prev_state['chosen_agent']['agent_private_price']

    return 'private_price', new_private_price


def update_private_alpha(params, substep, state_history, prev_state, policy_input):
    # Private alpha belief signal is a ramp
    #sign = (-1)**int((2*prev_state['timestep']/signal['period']))
    #new_private_alpha = prev_state['alpha'] + signal['dP']*sign

    # new_private_alpha = P0[0] + signal['dP'] * \
    #  np.sin(2*np.pi*prev_state['timestep']/signal['period'])

    # new_private_alpha = (random.randint(50, 100))/100

        # e is private alpha's bias towards public alpha

    b = 0.8 # high bias

    public_alpha_signal = 0.9
    private_alpha_signal = random.randint(0,50)/100
    new_public_alpha =  random.randint(0,50)/100
    new_private_alpha = (b)*new_public_alpha + (1-b)*private_alpha_signal

    #new_private_alpha = prev_state['chosen_agent']['agent_private_alpha']

    # print("new_private_alpha = ", new_private_alpha)
    return 'private_alpha', new_private_alpha


def update_agent_beliefs(params, substep, state_history, prev_state, policy_input):

    agent = prev_state['chosen_agent']
    timestep = prev_state['timestep']
    # params = params[0]
    alpha_bias = params['alpha_bias']
    price_bias = params['price_bias']

    #rv = np.random.normal(0, signal['sigma'])
    #new_private_price = price+price*rv
    #new_private_price = agent['agent_private_price']

    #new_private_price = agent['agent_private_price']
    #new_private_alpha = agent['agent_private_alpha']
    
    b_alpha = 0.0 # bias

    public_alpha_signal = 0.5 + ((1/1000)*timestep)
    private_alpha_signal = 0.5 + ((1/1000)*timestep)
    #private_alpha_signal = 0.5 - ((1/1000)*timestep)

    private_alpha = (b_alpha)*public_alpha_signal + (1-b_alpha)*private_alpha_signal

    b_price = 0.0 # bias

    public_price_signal = 0.5 + ((1/1000)*timestep)
    private_price_signal = 0.5 + ((1/1000)*timestep) 
    #private_price_signal = 1.5 - ((1/1000)*timestep)

    private_price = (b_price)*public_price_signal + (1-b_price)*private_price_signal

    agent['agent_private_price_signal'] = private_price_signal
    agent['agent_private_alpha_signal'] = private_alpha_signal
    agent['agent_public_price_signal'] = public_price_signal
    agent['agent_public_alpha_signal'] = public_alpha_signal
    
    agent['agent_private_price'] = private_price
    agent['agent_private_alpha'] = private_alpha

    #print("agent['agent_private_price'] = ", agent['agent_private_price'])
    #print("agent['agent_private_alpha'] = ", agent['agent_private_alpha'])

    return 'chosen_agent', agent
