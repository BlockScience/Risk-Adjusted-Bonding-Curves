import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def alpha_plot(experiments,test_title,T):
    agent_private_alpha_signal = []
    agent_public_alpha_signal = []
    agent_private_alpha = []
    
    df = experiments
    df = df[df['substep'] == df.substep.max()]
    df.fillna(0,inplace=True)

    for i in range (0,T): 
        agent_public_alpha_signal_list = []
        agent_public_alpha_signal_list.append(df.chosen_agent.values[i]['agent_public_alpha_signal'])
        agent_public_alpha_signal.append(np.mean(agent_public_alpha_signal_list))
        agent_private_alpha_signal_list= []
        agent_private_alpha_signal_list.append(df.chosen_agent.values[i]['agent_private_alpha_signal'])
        agent_private_alpha_signal.append(np.mean(agent_private_alpha_signal_list))
        agent_private_alpha_list = []
        agent_private_alpha_list.append(df.chosen_agent.values[i]['agent_private_alpha'])
        agent_private_alpha.append(np.mean(agent_private_alpha_list))
    public_alpha = df.alpha
    fig = plt.figure(figsize=(15, 10))
    plt.plot(range(0,T),agent_public_alpha_signal,label='Agent Public Alpha Signal', marker='o')
    plt.plot(range(0,T),agent_private_alpha_signal,label='Agent Private Alpha Signal',marker='o')
    plt.plot(range(0,T),agent_private_alpha,label='Agent Private Alpha',marker='*')
    plt.legend()
    plt.title(test_title)
    plt.xlabel('Timestep')
    plt.ylabel('Alpha')
    plt.show()
            
def reserve_supply(experiments,test_title,T):
    
    df = experiments
    df = df[df['substep'] == df.substep.max()]
    df.fillna(0,inplace=True)

    fig = plt.figure(figsize=(15, 10))
    plt.plot(range(0,T),df.reserve,label='Reserve',marker='o')
    plt.plot(range(0,T),df.supply,label='Supply',marker='*')
    
    plt.legend()
    plt.title(test_title)
    plt.xlabel('Timestep')
    plt.ylabel('Amount')

    plt.show()



def price(experiments,test_title,T):
    
    df = experiments
    df = df[df['substep'] == df.substep.max()]
    df.fillna(0,inplace=True)

    fig = plt.figure(figsize=(15, 10))
    plt.plot(range(0,T),df.spot_price,label='Spot Price',marker='+')
    plt.legend()
    plt.title(test_title)
    plt.xlabel('Timestep')
    plt.ylabel('Amount')

    plt.show()
    
    return 


def agent_payout_2(experiments,t):
    S_free = experiments.supply_free[t]
    S_0 = experiments.supply_0[t]
    S_1 = experiments.supply_1[t]
    agents_id = [0,1,2,3,4,5,6,7,9]
    payout_list = []
    for a in agents_id:
        q1 = experiments.agents[t].agent_attestations_1[a]
        q0 = experiments.agents[t].agent_attestations_0[a]
        s_free = experiments.agents[t].agent_supply_free[a]
        s1 = experiments.agents[t].agent_supply_1[a]
        s0 = experiments.agents[t].agent_supply_0[a]
        s = s_free + s1 + s0
        agent_private_alpha = experiments.agents[t].agent_private_alpha[a]
        Q0 = experiments.attestations_0[t]
        Q1 = 1 
        R = experiments.reserve[t]
        S = experiments.supply[t]
        C = 300000000 
        alpha = experiments.alpha[t]
        if alpha < 0.5:
            alpha = 0
        elif alpha > 0.5:
            alpha = 1
        T1 = (s_free/S)*(C*alpha + R)
        T2 = (s1/(S-S_0))*alpha*(C+R)
        T3 = (s0/(S-S_1))*(1-alpha)*(R)
        agent_payout = T1+T2+T3
        payout_list.append(agent_payout)

        arr2d = np.array(payout_list)

    arr1d = arr2d.flatten()

    x = agents_id
    payouts = arr1d

    x_pos = [i for i, _ in enumerate(x)]

    fig = plt.figure(figsize=(15, 10))
    plt.bar(x_pos, payouts, color='green')
    plt.xlabel("Agent ID")
    plt.ylabel("Payout amount (tokens)")
    plt.title("Agent and their Payouts")

    plt.xticks(x_pos, x)

    plt.show()

