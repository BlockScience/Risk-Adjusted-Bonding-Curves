import pandas as pd


def choose_agent(params, substep, state_history, prev_state):

    # Randomly sample one agent from all agents
    chosen_agent = prev_state['agents'].sample(n=1)
    print("CHOSEN AGENT = ", chosen_agent)

    return 'chosen_agent', chosen_agent
