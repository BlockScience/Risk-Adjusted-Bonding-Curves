import pandas as pd

from src.sim.model.sys_params import *

PRICE = 1
### NEED TO Refactor across params and configs
reserve = MONEY_RAISED[0]  # - C[0]
supply = KAPPA[0]*(reserve/PRICE)
supply_free = supply
invariant_V = (supply**KAPPA[0])/reserve
invariant_I = reserve + (C[0]*ALPHA[0])



number_of_agents = 5

PRIVATE_ALPHA = 0.1
PRIVATE_PRICE = 1.5

# Set initialization state variables for Attestations
Q = 40
Q1 = 20
Q0 = 20
S1 = 30  # Considering S = 600 and S_free = 200
S0 = 20  # Considering S = 600 and S_free = 200
r = 100    # Agent reserve, the amount of fiat tokens an agent starts with
s = 50
s1 = 3  # Considering s = 50 and s_free = 30
s0 = 2  # Considering s = 50 and s_free = 30
s_free = s - (s1+s0)

# Configure agents for agent-based model
agents_df = pd.DataFrame({
    'agent_attestations_1': 0,
    'agent_attestations_0': 0,
    'agent_reserve': r,
    # 'agent_supply': s,
    'agent_supply_1': s1,
    'agent_supply_0': s0,
    'agent_supply_free': s_free,
    'agent_private_alpha': PRIVATE_ALPHA,
    'agent_private_price': PRIVATE_PRICE}, index=[0])
agents_df = pd.concat([agents_df]*number_of_agents, ignore_index=True)
# Adding IDs to agents
agents_df.insert(0, 'id', range(0, len(agents_df)))

# 0.6, 0.7, 0.8, 0.9
agents_df['agent_private_alpha'] = 0.3, 0.4, 0.5, 0.6, 0.7
agents_df['agent_private_price'] = 0.5, 0.9, 1.0, 1.1, 1.5  # 0.2, 2, 3, 4, 6

# Put this in state_vars.py
initial_conditions = {
    'reserve': reserve,
    'pbar': PRICE,  # kappa*(reserve/supply), price is dR/dS = 1
    'realized_price': 0,
    'spot_price': PRICE,
    # 'private_price': 0,
    # 'private_alpha': 0,
    'kappa': 0,  # direct to initial kappa in params?
    'supply': supply,
    'alpha': ALPHA,  # direct to initial alpha in params?
    'alpha_bar': ALPHA,  # direct to initial alpha in params?

    # 'spot_alpha': 0,
    'supply_0': S0,
    'supply_1': S1,
    'supply_free': supply_free,
    'attestations': Q,
    'attestations_0': Q0,
    'attestations_1': Q1,
    'invariant_V': invariant_V,  # (supply**kappa)/reserve
    # (reserve + C*alpha) if alpha is directed to the initial alpha in params, this will change
    'invariant_I': invariant_I,
    # 'agent_attestations_1': 0,
    # 'agent_attestations_0': 0,
    # 'agent_reserve': r,
    # 'agent_supply': s,
    # 'agent_supply_1': s1,
    # 'agent_supply_0': s0,
    # 'agent_supply_free': s_free,
    'agents': agents_df,
    'chosen_agent': 0
}



print("Initial Conditions (config.py) : ", initial_conditions)