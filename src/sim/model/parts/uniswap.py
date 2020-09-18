def getInputPrice(input_amount, input_reserve, output_reserve, params):
    fee_numerator = params['fee_numerator']
    fee_denominator = params['fee_denominator']
    input_amount_with_fee = input_amount * fee_numerator
    numerator = input_amount_with_fee * output_reserve
    denominator = (input_reserve * fee_denominator) + input_amount_with_fee
    return int(numerator // denominator)

# For buying, not needed right now
def supply_tokens_added(params, substep, state_history, prev_state, policy_input):
    if params['ENABLE_BURN']:
        return ('UNI_supply', 0)
    else:
        tokens_sold = int(policy_input['amt_to_burn']) #amount of ETH being sold by the user
        token_supply = int(prev_state['UNI_supply'])
        return ('UNI_supply', token_supply + tokens_sold)


def reserve_redeemed(params, substep, state_history, prev_state, policy_input):
    if params['ENABLE_BURN']:
        return ('UNI_reserve', 0)
    else:
        tokens_sold = int(policy_input['amt_to_burn']) #amount of tokens being sold by the user
        uni_reserve = int(prev_state['UNI_reserve'])
        if tokens_sold == 0:
            return ('UNI_reserve', uni_reserve)
        else:
            token_supply = int(prev_state['UNI_supply'])
            reserve_redeemed = int(getInputPrice(tokens_sold, token_supply, uni_reserve, params))
            return ('UNI_reserve', uni_reserve - reserve_redeemed)
        


def compute_r(R, S, V, kappa, r, deltaS, policy_input):
    if V == 0:
        print("V IS ZERO")
    else:
        deltar = R-((S-deltaS)**kappa)/V

    r = r - policy_input['amt_to_bond'] + deltar
    return r


def compute_s_free(R, S, V, kappa, s_free, deltaR, policy_input, timestep):

    deltas = (V*(R+deltaR))**(1/kappa)-S

    s_free = s_free + deltas - policy_input['amt_to_burn']

    # TEST RANDOM DROP
    if timestep % 20 == 0:
        random_drop = 10
    else:
        random_drop = 0

    s_free = s_free + random_drop

    return s_free


def reserve_redeemed_to_agent(params, substep, state_history, prev_state, policy_input):
    """
    If uniswap instance is permitted, update reserve redeemed to agent here from burning their tokens
    Burn (supply) is already computed in the bondburn, because the tokens to burn would be the same regardless of where they are burned (assumed price and fees equal)
    """
    agent = prev_state['chosen_agent']
    if params['ENABLE_BURN']:
        return 'chosen_agent', agent
    else:
        tokens_sold = int(policy_input['amt_to_burn']) #amount of tokens being sold by the user
        uni_reserve = int(prev_state['UNI_reserve'])
        if tokens_sold == 0:
            return 'chosen_agent', agent
        else:
            token_supply = int(prev_state['UNI_supply'])
            reserve_redeemed = int(getInputPrice(tokens_sold, token_supply, uni_reserve, params))
            r = agent['agent_reserve']
            agent['agent_reserve'] = r + reserve_redeemed
            return  'chosen_agent', agent

