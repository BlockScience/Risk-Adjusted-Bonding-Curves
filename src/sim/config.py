from cadCAD.configuration import append_configs
from cadCAD.configuration.utils import config_sim

# from model.sys_params import params
# from model.state_variables import initial_conditions
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
append_configs(
    # dict containing variable names and initial values
    initial_state=initial_conditions,
    # dict containing state update functions
    partial_state_update_blocks=partial_state_update_block,
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
    c.initial_state['reserve'] = c.sim_config['M']['money_raised']


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
