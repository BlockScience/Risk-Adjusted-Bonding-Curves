from cadCAD.configuration import append_configs
from cadCAD.configuration.utils import config_sim

from .model.sys_params import params
from .model.state_variables import initial_conditions
from .model.partial_state_update_block import partial_state_update_blocks

from copy import deepcopy
from cadCAD import configs

time_periods_per_run = 4000
monte_carlo_runs = 1

### Put this in sys_params.py
params = {
    'starting_kappa': [2], #initial kappa
    'starting_alpha': [0.5, 1], #initial alpha
    'money_raised': [1000], # R+C
    'C': [700],
    'supply': []
}

kappa = [2]
reserve = money_raised - C
supply
alpha
C


### Put this in state_vars.py
initial_conditions = {
    'reserve': money_raised - C,
    'price': 1, ### kappa*(reserve/supply), price is dR/dS = 1
    'kappa': 0, ### direct to initial kappa in params?
    'supply': kappa*(reserve/price), 
    'price': kappa*(reserve/supply), ### kappa*(reserve/supply)
    'alpha': 0, ### direct to initial alpha in params?
    'supply_0': 0,
    'supply_1': 0,
    'supply_free': supply,
    'attestations_0': 0,
    'attestations_1': 0,
    'invariant_V': (supply**kappa)/reserve, ### (supply**kappa)/reserve
    'invariant_I': (reserve + C*alpha) ### (reserve + C*alpha) if alpha is directed to the initial alpha in params, this will change
}

simulation_parameters = config_sim({
    'T': range(time_periods_per_run),
    'N': monte_carlo_runs,
    'M': params
})

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The configurations above are packaged into a `Configuration` object
append_configs(
    initial_state=initial_conditions, #dict containing variable names and initial values
    partial_state_update_blocks=partial_state_update_blocks, #dict containing state update functions
    sim_configs=simulation_parameters #dict containing simulation parameters
)

for c in configs {
    c.initial_state = deepcopy(c.initial_state)
    c.initial_state['alpha'] = c.sim_config['M']['starting_alpha']
}
