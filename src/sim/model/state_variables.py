import pandas as pd

from src.sim.model.sys_params import *

# Set initialization state variables for Attestations

PRICE = 1
Q = 30000
Q1 = 100
Q0 = 30000
S1 = 100
S0 = 30000
r = 100  # Agent reserve, the amount of fiat tokens an agent starts with
s = 0
s1 = 0
s0 = 0
s_free = s - (s1+s0)


######## Just for initalization of variables ##########
####  Overwritten in configs.py for parameter sweeps with values in sys_params ######
reserve = (1-THETA[0])*MONEY_RAISED[0]
supply = KAPPA[0]*(reserve/PRICE)
supply_free = supply - (S0 + S1)
invariant_V = (supply**KAPPA[0])/reserve
invariant_I = reserve + (C[0]*ALPHA[0])

ALPHA = S1 * reserve / (S1 * reserve - S0 * reserve + S0*C[0])
# print("ALPHA = ", ALPHA)
KAPPA = invariant_I / (invariant_I - (C[0]*ALPHA))
# print("KAPPA = ", KAPPA)
##### Overwritten in configs.py for parameter sweeps with values in sys_params ######


########## AGENT INITIALIZATION ##########
number_of_agents = 2

PRIVATE_ALPHA = 0.5
PRIVATE_PRICE = 0.5

# Configure agents for agent-based model
agents_df = pd.DataFrame({
    'agent_attestations_1': 0,
    'agent_attestations_0': 0,
    'agent_reserve': r,
    'agent_supply_1': s1,
    'agent_supply_0': s0,
    'agent_supply_free': s_free,
    'agent_private_alpha': PRIVATE_ALPHA,
    'agent_private_price': PRIVATE_PRICE,    
    'agent_private_alpha_signal': 0,
    'agent_private_price_signal': 0,
    'agent_public_alpha_signal': 0,
    'agent_public_price_signal': 0}, index=[0])
agents_df = pd.concat([agents_df]*number_of_agents, ignore_index=True)
# Adding IDs to agents
agents_df.insert(0, 'id', range(0, len(agents_df)))

# 0.6, 0.7, 0.8, 0.9
# 0.3, 0.4, 0.5, 0.6, 0.7
# 0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1
agents_df['agent_private_alpha'] = 0.5, 0.5#, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5
# 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5
# 0.5, 0.9, 1.0, 1.1, 1.5  # 0.2, 2, 3, 4, 6
agents_df['agent_private_price'] = 0.5, 0.5#, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5
# 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5, 1.5

########## SYSTEM INITIALIZATION ##########
initial_conditions = {
    # Overwritten in configs.py with sys_params value for future parameter sweeps
    'reserve': reserve,
    'pbar': PRICE,  # kappa*(reserve/supply), price is dR/dS = 1
    'realized_price': 0,
    'spot_price': PRICE,
    'kappa': 0,
    'supply': supply,
    'alpha': ALPHA,
    'alpha_bar': ALPHA,
    'supply_0': S0,
    'supply_1': S1,
    'supply_free': supply_free,
    'attestations': Q,
    'attestations_0': Q0,
    'attestations_1': Q1,
    'invariant_V': invariant_V,  # (supply**kappa)/reserve
    'invariant_I': invariant_I,
    'agents': agents_df,
    'chosen_agent': 0,
    'public_alpha': 0
}


# print("Initial Conditions (config.py) : ", initial_conditions)
