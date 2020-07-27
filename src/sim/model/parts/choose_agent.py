import pandas as pd


def get_value(value):
    '''
    if value is array, then returns the first item, else returns value
    '''
    if isinstance(value, list):
        return value[0]

    return value


def choose_agent(params, substep, state_history, prev_state, policy_input):
    print(prev_state['agents'].tail())
    print('----------------------------')
    # Randomly sample one agent from all agents
    chosen_agent_df = prev_state['agents'].sample(n=1)
    print("CHOSEN AGENT = ", chosen_agent_df, 'Time ', prev_state['timestep'])

    chosen_agent = chosen_agent_df.to_dict('list')
    chosen_agent = {key: get_value(value)
                    for key, value in chosen_agent.items()}

    timestep = prev_state['timestep']
   # chosen_agent['picked'] = True

    return ('chosen_agent', chosen_agent)
