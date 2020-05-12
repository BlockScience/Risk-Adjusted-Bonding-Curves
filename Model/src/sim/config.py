from cadCAD.configuration import append_configs
from cadCAD.configuration.utils import config_sim

from .model.sys_params import params
from .model.state_variables import initial_conditions
from .model.partial_state_update_block import partial_state_update_blocks

from copy import deepcopy
from cadCAD import configs

time_periods_per_run = 4000
monte_carlo_runs = 1

KAPPA = [2]
PRICE = [1]
C = [700]
ALPHA = [0.5, 1]
MONEY_RAISED = [1000]

reserve = money_raised - C
supply = kappa*(reserve/price)
supply_free = supply
invariant_V = (supply**kappa)/reserve
invariant_I = reserve + (C*alpha)

### Put this in sys_params.py
params = {
    'starting_kappa': KAPPA, #initial kappa
    'starting_alpha': ALPHA, #initial alpha
    #'starting_price': price, 
    'money_raised': MONEY_RAISED, # R+C
    'C': C 
}

### Put this in state_vars.py
initial_conditions = {
    'reserve': reserve,
    'price': price, ### kappa*(reserve/supply), price is dR/dS = 1
    'realized_price': 0,
    'kappa': 0, ### direct to initial kappa in params?
    'supply': supply, 
    #'price': kappa*(reserve/supply), ### kappa*(reserve/supply)
    'alpha': 0, ### direct to initial alpha in params?
    'supply_0': 0,
    'supply_1': 0,
    'supply_free': supply_free,
    'attestations_0': 0,
    'attestations_1': 0,
    'invariant_V': invariant_V, ### (supply**kappa)/reserve
    'invariant_I': invariant_I ### (reserve + C*alpha) if alpha is directed to the initial alpha in params, this will change
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
  
    c.initial_state['kappa'] = c.sim_config['M']['starting_kappa']
    c.initial_state['alpha'] = c.sim_config['M']['starting_alpha']
    #c.initial_state['money_raised'] = c.sim_config['M']['starting_alpha']
    #c.initial_state['C'] = c.sim_config['M']['C']
}
