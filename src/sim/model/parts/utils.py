import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import pickle


def alpha_plot(experiments,test_title):
    agent_private_alpha_signal = []
    agent_public_alpha_signal = []
    agent_private_alpha = []
    df = experiments.dataset[0]
    df = df[df['substep'] == df.substep.max()]
    for i in range (0,100): 
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
    plt.plot(range(0,100),agent_public_alpha_signal,label='Agent Public Alpha Signal', marker='o')
    plt.plot(range(0,100),agent_private_alpha_signal,label='Agent Private Alpha Signal',marker='o')
    plt.plot(range(0,100),agent_private_alpha,label='Agent Private Alpha',marker='*')
    plt.legend()
    plt.title(test_title)
    plt.xlabel('Timestep')
    plt.ylabel('Alpha')
    plt.show()
    
    return agent_public_alpha_signal,agent_private_alpha_signal, agent_private_alpha
        
def reserve_supply(experiments,test_title):
    
    df = experiments.dataset[0][experiments.dataset[0]['substep'] == experiments.dataset[0].substep.max()]

    fig = plt.figure(figsize=(15, 10))
    plt.plot(range(0,100),df.reserve,label='Reserve',marker='o')
    plt.plot(range(0,100),df.supply,label='Supply',marker='*')
    
    plt.legend()
    plt.title(test_title)
    plt.xlabel('Timestep')
    plt.ylabel('Amount')

    plt.show()


def funds_from_bond(experiments,test_title):
    
    df = experiments.dataset[0][experiments.dataset[0]['substep'] == experiments.dataset[0].substep.max()]

    fig = plt.figure(figsize=(15, 10))
    plt.plot(range(0,100),df.funds_from_bond,label='Funds from Bonds',marker='+')
    plt.legend()
    plt.title(test_title)
    plt.xlabel('Timestep')
    plt.ylabel('Amount')

    plt.show()


def price(experiments,test_title):
    
    df = experiments.dataset[0][experiments.dataset[0]['substep'] == experiments.dataset[0].substep.max()]

    fig = plt.figure(figsize=(15, 10))
    plt.plot(range(0,100),df.spot_price,label='Spot Price',marker='+')
    plt.legend()
    plt.title(test_title)
    plt.xlabel('Timestep')
    plt.ylabel('Amount')

    plt.show()
    
    return df.spot_price
    
def agent_payout(experiments):
    t = 600
    S_free = experiments.dataset[0].supply_free[t]
    S_0 = experiments.dataset[0].supply_0[t]
    S_1 = experiments.dataset[0].supply_1[t]
    agents_id = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    payout_list = []
    for a in agents_id:
        q1 = experiments.dataset[0].agents[t].agent_attestations_1[a]
        q0 = experiments.dataset[0].agents[t].agent_attestations_0[a]
        s_free = experiments.dataset[0].agents[t].agent_supply_free[a]
        s1 = experiments.dataset[0].agents[t].agent_supply_1[a]
        s0 = experiments.dataset[0].agents[t].agent_supply_0[a]
        s = s_free + s1 + s0
        agent_private_alpha = experiments.dataset[0].agents[t].agent_private_alpha[a]
        Q0 = experiments.dataset[0].attestations_0[t]
        Q1 = 1 
        R = experiments.dataset[0].reserve[t]
        S = experiments.dataset[0].supply[t]
        C = 72000 
        alpha = experiments.dataset[0].alpha[t]
        if alpha < 0.5:
            alpha = 0
        elif alpha > 0.5:
            alpha = 1
        #print("s_free = ", s_free, "| S = ", S)
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
    
    return x_pos,payouts

def agent_payout_2(experiments):
    t = 600
    S_free = experiments.dataset[0].supply_free[t]
    S_0 = experiments.dataset[0].supply_0[t]
    S_1 = experiments.dataset[0].supply_1[t]
    agents_id = [0,1]
    payout_list = []
    for a in agents_id:
        q1 = experiments.dataset[0].agents[t].agent_attestations_1[a]
        q0 = experiments.dataset[0].agents[t].agent_attestations_0[a]
        s_free = experiments.dataset[0].agents[t].agent_supply_free[a]
        s1 = experiments.dataset[0].agents[t].agent_supply_1[a]
        s0 = experiments.dataset[0].agents[t].agent_supply_0[a]
        s = s_free + s1 + s0
        agent_private_alpha = experiments.dataset[0].agents[t].agent_private_alpha[a]
        Q0 = experiments.dataset[0].attestations_0[t]
        Q1 = 1 
        R = experiments.dataset[0].reserve[t]
        S = experiments.dataset[0].supply[t]
        C = 72000 
        alpha = experiments.dataset[0].alpha[t]
        if alpha < 0.5:
            alpha = 0
        elif alpha > 0.5:
            alpha = 1
        #print("s_free = ", s_free, "| S = ", S)
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

def load_experiment_data(test):
    with open('chimple_data/'+test+'/Alpha/agent_public_alpha_signal.pickle', 'rb') as filehandle:
        # read the data as binary data stream
        agent_public_alpha_signal = pickle.load(filehandle)

    with open('chimple_data/'+test+'/Alpha/agent_private_alpha_signal.pickle', 'rb') as filehandle:
        # read the data as binary data stream
        agent_private_alpha_signal = pickle.load(filehandle)
    
    with open('chimple_data/'+test+'/Price/spot_price.pickle', 'rb') as filehandle:
        # read the data as binary data stream
        spot_price = pickle.load(filehandle)
    
    with open('chimple_data/'+test+'/Payout/agent_id.pickle', 'rb') as filehandle:
        # read the data as binary data stream
        agent_id = pickle.load(filehandle)
    
    with open('chimple_data/'+test+'/Payout/payouts.pickle', 'rb') as filehandle:
        # read the data as binary data stream
        payouts = pickle.load(filehandle)
        
        
    return agent_public_alpha_signal,agent_private_alpha_signal,spot_price,agent_id,payouts

def private_alpha_summary(agent_private_alpha_signal_A,agent_private_alpha_signal_B,agent_private_alpha_signal_C,
                          agent_private_alpha_signal_D,agent_private_alpha_signal_E,agent_private_alpha_signal_F,
                          agent_private_alpha_signal_G,agent_private_alpha_signal_H):


    fig, ((ax1, ax2,ax3,ax4), (ax5, ax6,ax7,ax8)) = plt.subplots(nrows=2, ncols=4, 
                                                                 sharex=True, sharey=True,figsize=(15, 10))

    fig.suptitle('Agent Private Alpha Signal')

    ax1.plot(range(0,100),agent_private_alpha_signal_A,label='Test Case A')
    ax1.set_title('Test Case A')
    ax1.set(xlabel='Timestep', ylabel='Amount')

    ax2.plot(range(0,100),agent_private_alpha_signal_B,label='Test Case B')
    ax2.set_title('Test Case B')
    ax2.set(xlabel='Timestep', ylabel='Amount')

    ax3.plot(range(0,100),agent_private_alpha_signal_C,label='Test Case C')
    ax3.set_title('Test Case C')
    ax3.set(xlabel='Timestep', ylabel='Amount')

    ax4.plot(range(0,100),agent_private_alpha_signal_D,label='Test Case D')
    ax4.set_title('Test Case D')
    ax4.set(xlabel='Timestep', ylabel='Amount')

    ax5.plot(range(0,100),agent_private_alpha_signal_E,label='Test Case E')
    ax5.set_title('Test Case E')
    ax5.set(xlabel='Timestep', ylabel='Amount')

    ax6.plot(range(0,100),agent_private_alpha_signal_F,label='Test Case F')
    ax6.set_title('Test Case F')
    ax6.set(xlabel='Timestep', ylabel='Amount')

    ax7.plot(range(0,100),agent_private_alpha_signal_G,label='Test Case G')
    ax7.set_title('Test Case G')
    ax7.set(xlabel='Timestep', ylabel='Amount')

    ax8.plot(range(0,100),agent_private_alpha_signal_H,label='Test Case H')
    ax8.set_title('Test Case H')
    ax8.set(xlabel='Timestep', ylabel='Amount')
    plt.show()
    
def spot_price_summary(spot_price_A,spot_price_B,spot_price_C,spot_price_D,spot_price_E,spot_price_F,
                      spot_price_G,spot_price_H):

    fig, ((ax1, ax2,ax3,ax4), (ax5, ax6,ax7,ax8)) = plt.subplots(nrows=2, ncols=4, 
                                                                 sharex=True, sharey=True,figsize=(15, 10))

    fig.suptitle('Spot Price')

    ax1.plot(range(0,100),spot_price_A,label='Test Case A',color='r')
    ax1.set_title('Test Case A')
    ax1.set(xlabel='Timestep', ylabel='Amount')

    ax2.plot(range(0,100),spot_price_B,label='Test Case B',color='r')
    ax2.set_title('Test Case B')
    ax2.set(xlabel='Timestep', ylabel='Amount')

    ax3.plot(range(0,100),spot_price_C,label='Test Case C',color='r')
    ax3.set_title('Test Case C')
    ax3.set(xlabel='Timestep', ylabel='Amount')

    ax4.plot(range(0,100),spot_price_D,label='Test Case D',color='r')
    ax4.set_title('Test Case D')
    ax4.set(xlabel='Timestep', ylabel='Amount')

    ax5.plot(range(0,100),spot_price_E,label='Test Case E',color='r')
    ax5.set_title('Test Case E')
    ax5.set(xlabel='Timestep', ylabel='Amount')

    ax6.plot(range(0,100),spot_price_F,label='Test Case F',color='r')
    ax6.set_title('Test Case F')
    ax6.set(xlabel='Timestep', ylabel='Amount')

    ax7.plot(range(0,100),spot_price_G,label='Test Case G',color='r')
    ax7.set_title('Test Case G')
    ax7.set(xlabel='Timestep', ylabel='Amount')

    ax8.plot(range(0,100),spot_price_H,label='Test Case H',color='r')
    ax8.set_title('Test Case H')
    ax8.set(xlabel='Timestep', ylabel='Amount')
    plt.show()
    
def agent_payout_summary(agent_id_A,payouts_A,agent_id_B,payouts_B,agent_id_C,payouts_C,agent_id_D,payouts_D,
                        agent_id_E,payouts_E,agent_id_F,payouts_F,agent_id_G,payouts_G,agent_id_H,payouts_H):
    
    fig, ((ax1, ax2,ax3,ax4), (ax5, ax6,ax7,ax8)) = plt.subplots(nrows=2, ncols=4, 
                                                             sharex=True, sharey=False,figsize=(15, 10))

    fig.suptitle('Agent Payouts')


    ax1.bar(agent_id_A, payouts_A,label='Test Case A',color='g')
    ax1.set_title('Test Case A')
    ax1.set(xlabel='Agent ID', ylabel='Amount')

    ax2.bar(agent_id_B, payouts_B,label='Test Case B',color='g')
    ax2.set_title('Test Case B')
    ax2.set(xlabel='Agent ID')

    ax3.bar(agent_id_C, payouts_C,label='Test Case C',color='g')
    ax3.set_title('Test Case C')
    ax3.set(xlabel='Agent ID')

    ax4.bar(agent_id_D, payouts_D,label='Test Case D',color='g')
    ax4.set_title('Test Case D')
    ax4.set(xlabel='Agent ID')

    ax5.bar(agent_id_E, payouts_E,label='Test Case E',color='g')
    ax5.set_title('Test Case E')
    ax5.set(xlabel='Agent ID', ylabel='Amount')

    ax6.bar(agent_id_F, payouts_F,label='Test Case F',color='g')
    ax6.set_title('Test Case F')
    ax6.set(xlabel='Agent ID')

    ax7.bar(agent_id_G, payouts_G,label='Test Case G',color='g')
    ax7.set_title('Test Case G')
    ax7.set(xlabel='Agent ID')

    ax8.bar(agent_id_H, payouts_H,label='Test Case H',color='g')
    ax8.set_title('Test Case H')
    ax8.set(xlabel='Agent ID')
    plt.show()