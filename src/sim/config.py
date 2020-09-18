from cadCAD.configuration import Experiment #append_configs # 4.18: append_configs. Later: Experiment
from cadCAD.configuration.utils import config_sim

from src.sim.model.state_variables import initial_conditions
from src.sim.model.partial_state_update_block import partial_state_update_block
from src.sim.model.sys_params import params

from src.sim.sim_setup import SIMULATION_TIME_STEPS, MONTE_CARLO_RUNS

from copy import deepcopy
from cadCAD import configs

sim_config = config_sim({
    'T': range(SIMULATION_TIME_STEPS),
    'N': MONTE_CARLO_RUNS,
    'M': params
})

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# The configurations above are packaged into a `Configuration` object

###### 4.18 conversion #######################
exp = Experiment()
exp.append_configs(
###### 4.18 conversion #######################
    # dict containing variable names and initial values
    initial_state=initial_conditions,
    # dict containing state update functions
    partial_state_update_blocks=partial_state_update_block,
    # dict containing simulation parameters
    sim_configs=sim_config
)

# pprint(configs)

for c in configs:
    c.initial_state = deepcopy(c.initial_state)

    print("Params (config.py) : ", c.sim_config['M'])

    c.initial_state['kappa'] = c.sim_config['M']['starting_kappa']
    c.initial_state['alpha'] = c.sim_config['M']['starting_alpha']
    c.initial_state['reserve'] = c.sim_config['M']['money_raised']
    c.initial_state['supply'] = c.initial_state['kappa'] * \
        c.sim_config['M']['money_raised'] / c.initial_state['spot_price']
    c.initial_state['supply_free'] = c.initial_state['supply']
    c.initial_state['invariant_V'] = (
        c.initial_state['supply']**c.initial_state['kappa']) / c.initial_state['reserve']
    c.initial_state['invariant_I'] = c.initial_state['reserve'] + \
        (c.sim_config['M']['C'] * c.initial_state['alpha'])
