from cadCAD.configuration import append_configs
from cadCAD.configuration.utils import config_sim

# from model.sys_params import params
# from model.state_variables import initial_conditions
from src.sim.model.partial_state_update_block import partial_state_update_blocks

from copy import deepcopy
from cadCAD import configs

import pandas as pd
import itertools

time_periods_per_run = 100
monte_carlo_runs = 2
E = 0.45  # to be reviewed

KAPPA = [2]
PRICE = 1
C = [2000]
ALPHA = [0.5]
MONEY_RAISED = [1000]
PERIOD = [2000]

# New price singal : Determines signal shape for agent's behaviour heuristic on price
# rules_price = ["martin"] #, "step"]  # , "ramp", "sin"]

rules_price = ["martin", "step"]  # , "ramp", "sin"]
# rules_price = ["martin", "step", "ramp", "sin"]

# Set initialization state variables for Attestations
Q = 40
Q1 = 20
Q0 = 20
S1 = 30  # Considering S = 600 and S_free = 200
S0 = 20  # Considering S = 600 and S_free = 200
r = 50    # Agent reserve, the amount of fiat tokens an agent starts with
s = 50
s1 = 3  # Considering s = 50 and s_free = 30
s0 = 2  # Considering s = 50 and s_free = 30
s_free = s - (s1+s0)

# reserve = 300 # MONEY_RAISED[0] - C[0]
# supply = 600 #KAPPA[0]*(reserve/PRICE)
# supply_free = supply
# invariant_V = 1200 #(supply**KAPPA[0])/reserve
# invariant_I = 650 #reserve + (C[0]*ALPHA[0])

reserve = MONEY_RAISED[0]  # - C[0]
supply = KAPPA[0]*(reserve/PRICE)
supply_free = supply
invariant_V = (supply**KAPPA[0])/reserve
invariant_I = reserve + (C[0]*ALPHA[0])

print()
# print(type(MONEY_RAISED))
# print(MONEY_RAISED)
# print()

# E = [0.1, 0.2, 0.3]
E = [0.2]

factors = [rules_price, KAPPA, E]
product = list(itertools.product(*factors))
rules_price, KAPPA, E = zip(*product)
rules_price = list(rules_price)
KAPPA = list(KAPPA)
E = list(E)


# Put this in sys_params.py
params = {
    'starting_kappa': KAPPA,  # initial kappa
    'starting_alpha': ALPHA,  # initial alpha
    # 'starting_price': price,
    'money_raised': MONEY_RAISED,  # reserve + C
    'C': C,  # Commited outcome payout
    'f': [0.03],  # param to control certainty of alpha at extremes
    'm': [0.15],  # param to modulate curvature of alpha threshold band
    'beta': [0.9],
    'dust': [10**-8],
    'period': PERIOD,
    'rules_price': rules_price,
    'E': E
}

number_of_agents = 2

PRIVATE_ALPHA = 0.1
PRIVATE_PRICE = 0.2

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

agents_df['agent_private_alpha'] = 0.1, 0.9  # 0.6, 0.7, 0.8, 0.9
agents_df['agent_private_price'] = 0.2, 20

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


sim_config = config_sim({
    'T': range(time_periods_per_run),
    'N': monte_carlo_runs,
    'M': params
})

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The configurations above are packaged into a `Configuration` object
append_configs(
    # dict containing variable names and initial values
    initial_state=initial_conditions,
    # dict containing state update functions
    partial_state_update_blocks=partial_state_update_blocks,
    # dict containing simulation parameters
    sim_configs=sim_config
)

# pprint(configs)
#
for c in configs:
    c.initial_state = deepcopy(c.initial_state)

    print("Params (config.py) : ", c.sim_config['M'])

    c.initial_state['kappa'] = c.sim_config['M']['starting_kappa']
    c.initial_state['alpha'] = c.sim_config['M']['starting_alpha']
    #c.initial_state['money_raised'] = c.sim_config['M']['starting_alpha']
    #c.initial_state['C'] = c.sim_config['M']['C']


""" state_variables = {}
agents = {}
for i in range(50):
    agent['agent_'+str(i)] = {
        'attestations_1': 0,
        'attestations_0': 0,
        'reserve': r,
        'supply': s,
        'supply_1': s1,
        'supply_0': s0,
        'supply_free': s_free
    } """
