import pandas as pd


def get_value(value):
    if isinstance(value, list):
        return value[0]

    return value


def choose_agent(params, substep, state_history, prev_state, policy_input):

    timestep = prev_state['timestep']

    agent = timestep % 10

    chosen_agent = prev_state['agents'].iloc[agent].to_dict()
    chosen_agent = {key: get_value(value)
                    for key, value in chosen_agent.items()}



    return ('chosen_agent', chosen_agent)

# 10 agents as we have it is fine
# 14 days where each day each participant gets 1xCHF
# each day the 10 participants all buy tokens on the boding curve with their 1xCHF
# after 14 days the bond closes because the project is over (succeeds)
# because the project wasn't actually spending any funds, the total amount of reward will in fact be the C + reserve