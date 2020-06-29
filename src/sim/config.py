from cadCAD.configuration import append_configs
from cadCAD.configuration.utils import config_sim

# from model.sys_params import params
# from model.state_variables import initial_conditions
from src.sim.model.partial_state_update_block import partial_state_update_blocks

from copy import deepcopy
from cadCAD import configs

time_periods_per_run = 400
monte_carlo_runs = 1
E = 0.45  # to be reviewed


KAPPA = [2]
PRICE = 1
C = [700]
ALPHA = [0.5]
MONEY_RAISED = [1000]
PERIOD = [2000]
Q1 = 1
Q0 = 1
r = 50  # Agent reserve, the amount of fiat tokens an agent starts with

reserve = MONEY_RAISED[0] - C[0]
supply = KAPPA[0]*(reserve/PRICE)
supply_free = supply
invariant_V = (supply**KAPPA[0])/reserve
invariant_I = reserve + (C[0]*ALPHA[0])

print()
print(type(MONEY_RAISED))
print(MONEY_RAISED)
print()
# Put this in sys_params.py
params = {
    'starting_kappa': KAPPA,  # initial kappa
    'starting_alpha': ALPHA,  # initial alpha
    # 'starting_price': price,
    'money_raised': MONEY_RAISED,  # R+C
    'C': C,
    'period': PERIOD
}

# Put this in state_vars.py
initial_conditions = {
    'reserve': reserve,
    'price': PRICE,  # kappa*(reserve/supply), price is dR/dS = 1
    'realized_price': 0,
    'spot_price': PRICE,
    'private_price': 0,
    'private_alpha': 0,
    'kappa': 0,  # direct to initial kappa in params?
    'supply': supply,
    'alpha': ALPHA,  # direct to initial alpha in params?
    # 'spot_alpha': 0,
    'supply_0': 0,
    'supply_1': 0,
    'supply_free': supply_free,
    'attestations_0': Q0,
    'attestations_1': Q1,
    'invariant_V': invariant_V,  # (supply**kappa)/reserve
    # (reserve + C*alpha) if alpha is directed to the initial alpha in params, this will change
    'invariant_I': invariant_I,
    'agent_attestations_1': 0,
    'agent_attestations_0': 0,
    'agent_reserve': r,
    'agent_supply': 0,
    'agent_supply_1': 0,
    'agent_supply_0': 0
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
