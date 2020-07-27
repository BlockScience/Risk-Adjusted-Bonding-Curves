import pandas as pd


def put_agent_back_to_df(params, substep, state_history, prev_state, policy_input):
    chosen_agent = prev_state['chosen_agent']

#    print('the type of idx ' + str(type(chosen_agent_id)) +
#          ' the value is '+str(chosen_agent_id))
    chosen_agent_df = pd.DataFrame(
        chosen_agent, index=[int(chosen_agent['id'])])

  #  print('Agent after a timestep:::' + chosen_agent_df.to_string())
    agents_df = prev_state['agents']
    agents_df.update(chosen_agent_df)

  #  print('Agent combined:::' + agents_df.to_string())

    return "agents", agents_df
