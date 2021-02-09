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

def public_alpha(experiments,test_title,T):
    
    df = experiments
    df = df[df['substep'] == df.substep.max()]
    df.fillna(0,inplace=True)

    fig = plt.figure(figsize=(15, 10))
    plt.plot(range(0,T),df.public_alpha,label='Public Alpha',marker='o')
    
    plt.legend()
    plt.title(test_title)
    plt.xlabel('Timestep')
    plt.ylabel('Amount')

    plt.show()
def alpha(experiments,test_title,T):
    
    df = experiments
    df = df[df['substep'] == df.substep.max()]
    df.fillna(0,inplace=True)

    fig = plt.figure(figsize=(15, 10))
    plt.plot(range(0,T),df.alpha,label='Alpha',marker='o')
    
    plt.legend()
    plt.title(test_title)
    plt.xlabel('Timestep')
    plt.ylabel('Amount')

    plt.show()
    
def supply_plot(experiments,test_title,T):
    
    df = experiments
    df = df[df['substep'] == df.substep.max()]
    df.fillna(0,inplace=True)

    fig = plt.figure(figsize=(15, 10))
    # plt.plot(range(0,T),df.reserve,label='Reserve',marker='o')
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

def agent_payout_calc(experiments,t, invest_list, initial_supply, C):
    """
    For CWU Payout
    """
    # print(experiments.agents[t])
    # C = 68100
    S_free = experiments.supply_free[t]
    S_0 = experiments.supply_0[t]
    S_1 = experiments.supply_1[t]
    agents_id = [0,1,2,3]
    payout_list = []
    no_R_payout_list = []
    # for a in agents_id:
    #     # print(experiments.agents[t])
    #     q1 = experiments.agents[t].agent_attestations_1[a]
    #     q0 = experiments.agents[t].agent_attestations_0[a]
    #     s_free = experiments.agents[t].agent_supply_free[a]
    for a in agents_id:
        # print(experiments.agents[t])
        q1 = experiments.agents[t].agent_attestations_1[a]
        q0 = experiments.agents[t].agent_attestations_0[a]
        s_free = experiments.agents[t].agent_supply_free[a]
        # print(a)
        # print('s_free', s_free)
        s1 = experiments.agents[t].agent_supply_1[a]
        s0 = experiments.agents[t].agent_supply_0[a]
        s = s_free + s1 + s0
        # print('s ', s)
        # print("s_free ", s_free)
        agent_private_alpha = experiments.agents[t].agent_private_alpha[a]
        Q0 = experiments.attestations_0[t]
        Q1 = 1 
        R = experiments.reserve[t]

        S = experiments.supply[t] - initial_supply # subtract initial amount No longer applicable, but can enter 0 and is unaffected
        # print(S)
        alpha = experiments.alpha[t]
        # TEMP TO SHOW A POINT
        alpha = 1
        # TEMP TO SHOW A POINT
        if alpha < 0.4:
            alpha = 0
        elif alpha >= 0.4:
            alpha = 1
        T1 = (s_free/S)*(C*alpha + R)
        # T2 = (s1/(S-S_0))*alpha*(C+R)
        # T3 = (s0/(S-S_1))*(1-alpha)*(R)

        agent_payout = T1
        payout_list.append(agent_payout)
        arr2d = np.array(payout_list)
        
        no_R_payout = (s_free/S)*(C*alpha)
        no_R_payout_list.append(no_R_payout)
        arr2d_no_R = np.array(no_R_payout_list)
        # print(no_R_payout)
    arr1d = arr2d.flatten()
    arr1d_no_R = arr2d_no_R.flatten()
    # print(arr1d_no_R, type(arr1d_no_R))
    S_zero = experiments.supply[0] #- initial_supply # subtract initial amount
    
    hatch_supply = S_zero #* (1 - experiments.alpha[0])
    hatch_payout_no_R = hatch_supply /  experiments.supply[t] * C
    arr1d_no_R_with_hatch = np.insert(arr1d_no_R, 0, hatch_payout_no_R)
    hatch_payout = hatch_supply /  experiments.supply[t] * (C + experiments.reserve[t])

    payouts = arr1d
    payouts_with_hatch = np.insert(arr1d, 0, hatch_payout)
    # print(payouts)
    investment = invest_list.copy()
    hatch = experiments.reserve[0]
    # investment[0] = investment[0] #+ hatch
    investment.insert(0,hatch)
    # print(invest_list)
    # print(np.sum(no_R_payout_list))
    # print(np.sum(no_R_payout_list)+hatch_payout_no_R)

    return investment, arr1d_no_R_with_hatch, payouts_with_hatch

def agent_payout_plot(experiments,t, invest_list, initial_supply, C):
    """
    For Plotting CWU Payout
    """
    investment, arr1d_no_R_with_hatch, payouts_with_hatch = agent_payout_calc(experiments,t, invest_list, initial_supply, C)
    # x = agents_id
    x = [0,1,2,3,4]
    x_pos = [i for i, _ in enumerate(x)]
    x_pos2 = [i+0.25 for i, _ in enumerate(x)]
    x_pos3 = [i-0.25 for i, _ in enumerate(x)]
   
    fig = plt.figure(figsize=(15, 10))
    
    plt.bar(x_pos3, investment, color='red', width=0.25)
    plt.bar(x_pos, arr1d_no_R_with_hatch, color='blue', width=0.25)
    plt.bar(x_pos2,payouts_with_hatch, color='green', width=0.25)

    plt.legend(['Invested', 'Outcome Share', 'Outcome + Reserve Share'])

    plt.xlabel("Agent ID")
    plt.ylabel("Payout amount")
    plt.title("Agents Spend and Return")
    plt.xticks(x_pos, ['Hatch', '0', '1', '2', '3'])

    # plt.xticks(x_pos, x)
    # plt.xlabel(['Hatch', '0', '1', '2', '3'])
    return plt.show()

def summary_table(experiments,t, invest_list, initial_supply, C):
    
    investment, arr1d_no_R_with_hatch, payouts_with_hatch = agent_payout_calc(experiments,t, invest_list, initial_supply, C)
    agent_ids = ['Hatch', '0', '1', '2', '3']
    # print(invest_list)
    results_table=pd.DataFrame(index = agent_ids)
    results_table.index.name = 'Agent ID'
    results_table['Investment'] = investment
    results_table['Return'] = arr1d_no_R_with_hatch
    results_table['ROI %'] = 100 * (results_table.Return - results_table.Investment) / results_table.Investment
    
    return results_table.round(1)   
    
def agent_ROI(experiments,t):
    S_free = experiments.supply_free[t]
    S_0 = experiments.supply_0[t]
    S_1 = experiments.supply_1[t]
    agents_id = [0,1,2,3,4,5,6,7,8,9]
    payout_list = []
    roi = []
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
        #roi.append(((s_free / S_free) * (C + R) - 14000000) / 14000000)
        roi_0 = (s_free * experiments.spot_price.values.mean()) - (14000000 * experiments.spot_price.values[0]) / 14000000 
        roi.append(roi_0 * 100)

        arr2d = np.array(roi)

    arr1d = arr2d.flatten()

    x = agents_id
    return_on_investments = arr1d

    x_pos = [i for i, _ in enumerate(x)]

    fig = plt.figure(figsize=(15, 10))
    plt.bar(x_pos, return_on_investments, color='green')
    plt.xlabel("Agent ID")
    plt.ylabel("ROI")
    plt.title("Agent and their ROI")

    plt.xticks(x_pos, x)

    plt.show()

    
# def agent_profit(experiments,t):
#     S_free = experiments.supply_free[t]
#     S_0 = experiments.supply_0[t]
#     S_1 = experiments.supply_1[t]
#     agents_id = [0,1,2,3,4,5,6,7,9]
#     payout_list = []
#     profits = []
#     for a in agents_id:
#         q1 = experiments.agents[t].agent_attestations_1[a]
#         q0 = experiments.agents[t].agent_attestations_0[a]
#         s_free = experiments.agents[t].agent_supply_free[a]
#         s1 = experiments.agents[t].agent_supply_1[a]
#         s0 = experiments.agents[t].agent_supply_0[a]
#         s = s_free + s1 + s0
#         agent_private_alpha = experiments.agents[t].agent_private_alpha[a]
#         Q0 = experiments.attestations_0[t]
#         Q1 = 1 
#         R = experiments.reserve[t]
#         S = experiments.supply[t]
#         C = 300000000 
#         alpha = experiments.alpha[t]
#         if alpha < 0.5:
#             alpha = 0
#         elif alpha > 0.5:
#             alpha = 1
#         T1 = (s_free/S)*(C*alpha + R)
#         T2 = (s1/(S-S_0))*alpha*(C+R)
#         T3 = (s0/(S-S_1))*(1-alpha)*(R)
#         agent_payout = T1+T2+T3
#         payout_list.append(agent_payout)
#         profits.append(agent_payout - 14000000)

#         arr2d = np.array(profits)

#     arr1d = arr2d.flatten()

#     x = agents_id
#     profit = arr1d

#     x_pos = [i for i, _ in enumerate(x)]

#     fig = plt.figure(figsize=(15, 10))
#     plt.bar(x_pos, profit, color='green')
#     plt.xlabel("Agent ID")
#     plt.ylabel("Profit")
#     plt.title("Agents and their Profits")

#     plt.xticks(x_pos, x)

#     plt.show()

def agent_profit(experiments,t):
    S_free = experiments.supply_free[t]
    S_0 = experiments.supply_0[t]
    S_1 = experiments.supply_1[t]
    agents_id = [0,1,2,3,4,5,6,7,8,9]
    payout_list = []
    profits = []
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
        S = experiments.supply[t] - 1000000 # subtract initial amount
        C = 300000000 
        alpha = experiments.alpha[t]
        if alpha < 0.4:
            alpha = 0
        elif alpha > 0.4:
            alpha = 1
        T1 = (s_free/S)*(C*alpha + R)
        # T2 = (s1/(S-S_0))*alpha*(C+R)
        # T3 = (s0/(S-S_1))*(1-alpha)*(R)
        agent_payout = T1
        payout_list.append(agent_payout)
        profits.append(agent_payout - 14000000)

        arr2d = np.array(profits)

    arr1d = arr2d.flatten()

    x = agents_id
    profit = arr1d

    x_pos = [i for i, _ in enumerate(x)]

    fig = plt.figure(figsize=(15, 10))
    plt.bar(x_pos, profit, color='green')
    plt.xlabel("Agent ID")
    plt.ylabel("Profit")
    plt.title("Agents and their Profits")

    plt.xticks(x_pos, x)

    plt.show()
