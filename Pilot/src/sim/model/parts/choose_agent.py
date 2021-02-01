import pandas as pd


def get_value(value):
    if isinstance(value, list):
        return value[0]

    return value


def choose_agent(params, substep, state_history, prev_state, policy_input):

    timestep = prev_state['timestep']

    #agent = timestep % 10
   
    # print ("TIMESTEP = ", timestep)
    if timestep >= 0 and timestep < 90:
        agent = 0
        # print("AGENT 0 = ", agent)
    elif timestep >= 90 and timestep < 180: 
        agent = 1
        # print("AGENT 1 = ", agent)
    elif timestep >= 180 and timestep < 270: 
        agent = 2
        # print("AGENT 2 = ", agent)
    elif timestep >= 270: 
        agent = 3
    #     # print("AGENT 3 = ", agent)
        
        # print ("TIMESTEP = ", timestep)
    # if  timestep < 90:
    #     agent = 4
    #     # print("AGENT 0 = ", agent)

    # elif  timestep >= 90 and timestep < 180:
    #     agent = 0
    #     # print("AGENT 0 = ", agent)

    # elif timestep >= 180 and timestep < 270:
    #     agent = 1
    #     # print("AGENT 0 = ", agent)
    # elif timestep >= 270 and timestep < 360: 
    #     agent = 2
    #     # print("AGENT 1 = ", agent)
    # elif timestep >= 360: # and timestep < 360: 
    #     agent = 3
        # print("AGENT 2 = ", agent)
    # elif timestep >= 3600: 
    #     agent = 3
    #     # print("AGENT 3 = ", agent)


    # print("PREV STATE AGENTS = ", prev_state['agents'])
    #print("I LOC AGENT = ", prev_state['agents'].iloc[agent].to_dict())

    chosen_agent = prev_state['agents'].iloc[agent].to_dict()
    chosen_agent = {key: get_value(value)
                    for key, value in chosen_agent.items()}

#############    #####################################
    if agent == 0:
        chosen_agent['agent_reserve'] =  chosen_agent['agent_reserve'] #+ 100

    return ('chosen_agent', chosen_agent)

# 10 agents as we have it is fine
# 14 days where each day each participant gets 1xCHF
# each day the 10 participants all buy tokens on the boding curve with their 1xCHF
# after 14 days the bond closes because the project is over (succeeds)
# because the project wasn't actually spending any funds, the total amount of reward will in fact be the C + reserve