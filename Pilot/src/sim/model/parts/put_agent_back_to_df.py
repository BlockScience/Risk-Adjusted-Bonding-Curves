import pandas as pd


def put_agent_back_to_df(params, substep, state_history, prev_state, policy_input):
    chosen_agent = prev_state['chosen_agent']


    chosen_agent_df = pd.DataFrame(
        chosen_agent, index=[int(chosen_agent['id'])])

    agents_df = prev_state['agents']
    agents_df.update(chosen_agent_df)


    return "agents", agents_df
