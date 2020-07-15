def putting_the_updated_agent_back_to_its_god_given_home_in_the_dataframe(params, substep, state_history, prev_state, policy_input):
    chosen_agent = prev_state['chosen_agent']
    agents_df = prev_state['agents']
    agents_as_array = agents_df.to_numpy()

    chosen_agent_idx = chosen_agent.index
    chosen_agent_as_array = chosen_agent.to_numpy()

    agents_as_array[chosen_agent_idx] = chosen_agent_as_array
    # should be updating agents_df
    #need cols=
    agents_df = pd.DataFrame(columns=['agent_attestations_1',
                          'agent_attestations_0',
                          'agent_reserve',
                          'agent_supply',
                          'agent_supply_1',
                          'agent_supply_0',
                          'agent_supply_free'],data=agents_as_array)

    return "agents", agents_df
