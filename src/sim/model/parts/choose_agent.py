import pandas as pd


def choose_agent(params, substep, state_history, prev_state, policy_input):

    # Randomly sample one agent from all agents
    chosen_agent = prev_state['agents'].sample(n=1)
    print("CHOSEN AGENT = ", chosen_agent, 'Time ', prev_state['timestep'])

    chosen_agent_as_array = chosen_agent.to_numpy()

    chosen_agent_as_array = 7
    print('Still working')
    return ('chosen_agent', chosen_agent)
