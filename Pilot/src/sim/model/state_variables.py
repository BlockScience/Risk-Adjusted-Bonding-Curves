import pandas as pd

from src.sim.model.sys_params import *

# Set initialization state variables for Attestations

PRICE = 1
Q = 30000
Q1 = 100
Q0 = 30000
S1 = 1 #0 #100
S0 = 100 #0 #30000
r = 0  # Agent reserve, the amount of fiat tokens an agent starts with
s = 0
s1 = 0
s0 = 0
s_free = s - (s1+s0)

C = C[0]

r1 = 30000 # reserve of agent 1; represents Tranche 1
r2 = 10000 # reserve of agent 2; represents Tranche 2
r3 = 10000 # reserve of agent 3; represents Tranche 3
r4 = 10000 # reserve of agent 4; represents Tranche 4

#### FIX ALPHA, KAPPA Dependent VERSION 
#### FIX KAPPA, ALPHA Dependent VERSION 

# ALPHA = ALPHA[0] #### FIX KAPPA, ALPHA Dependent VERSION 
# ALPHA = 0.5 #### FIX ALPHA, KAPPA Dependent VERSION 


KAPPA = KAPPA[0] #### FIX KAPPA, ALPHA Dependent VERSION 
######## Just for initalization of variables ##########
####  Overwritten in configs.py for parameter sweeps with values in sys_params ######
reserve = 1 # (1-THETA[0])*MONEY_RAISED[0]

# KAPPA = 1 + (C * ALPHA / reserve) #### FIX ALPHA, KAPPA Dependent VERSION 

supply = KAPPA*(reserve/PRICE)
# IF P0 = 1 , then Supply should equal Reserve
# supply = reserve
supply_free = supply  - (S0 + S1)
invariant_V = (supply**KAPPA)/reserve

ALPHA = S1 * reserve / (S1 * reserve - S0 * reserve + S0*C) #### FIX KAPPA, ALPHA Dependent VERSION 

invariant_I = reserve + (C*ALPHA)

# ALPHA = 0.5
# print("ALPHA = ", ALPHA)
#invariant_I / (invariant_I - (C[0]*ALPHA))
# print("KAPPA = ", KAPPA)
##### Overwritten in configs.py for parameter sweeps with values in sys_params ######
invariant_I = reserve + (C*ALPHA)

# Apply Alpha Initialization Ratio
S1 = ((C * ALPHA) - (reserve * ALPHA)) / (reserve * (1 - ALPHA)) * S0

# invariant_I = (KAPPA * C[0]*ALPHA) / (KAPPA - 1)

# invariant_I = KAPPA * reserve # equates as above

########## AGENT INITIALIZATION ##########
number_of_agents = 4

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

agents_df['agent_private_alpha'] = 0.5, 0.5, 0.5, 0.5
agents_df['agent_private_price'] = 0.5, 0.5, 0.5, 0.5
agents_df['agent_reserve'] = 30000, 10000, 10000, 10000


########## SYSTEM INITIALIZATION ##########
initial_conditions = {
    # Overwritten in configs.py with sys_params value for future parameter sweeps
    'reserve': reserve,
    'pbar': PRICE,  # kappa*(reserve/supply), price is dR/dS = 1
    'realized_price': 0,
    'spot_price': PRICE,
    # 'kappa': 0,
    'kappa': KAPPA,
    'supply': supply,
    'alpha': ALPHA,
    # 'alpha': ALPHA[0],

    'alpha_bar': ALPHA,
    # 'alpha_bar': ALPHA[0],
    
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
