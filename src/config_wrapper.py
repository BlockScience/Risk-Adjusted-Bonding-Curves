from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import Experiment
import importlib

class ConfigWrapper:
    '''
    The ConfigWrapper allows you to pass a model as an argument, and update the simulation configuration.
    Maps (params, states) would be merge updated, and all other options are overrides.
    '''
    def __init__(
            self,
            model,
            N=None,
            T=None,
            M={},
            initial_state={},
            partial_state_update_blocks=None,
            env_processes={},
            exp=Experiment()
        ):
        m_state_variables = importlib.import_module(f'{model.__name__}.model.state_variables').initial_conditions
        m_psubs = importlib.import_module(f'{model.__name__}.model.partial_state_update_block').partial_state_update_block
        m_params = importlib.import_module(f'{model.__name__}.model.sys_params').params
        m_sim_params = importlib.import_module(f'{model.__name__}.sim_setup')
        
        self.N = N if N else m_sim_params.MONTE_CARLO_RUNS
        self.T = T if T else range(m_sim_params.SIMULATION_TIME_STEPS)
        
        m_params.update(M)
        self.M = m_params
        
        m_state_variables.update(initial_state)
        self.initial_state = m_state_variables
        
        self.partial_state_update_blocks = partial_state_update_blocks if partial_state_update_blocks else m_psubs
        self.env_processes = env_processes
        self.exp = exp

    def get_config(self):
        return config_sim(
            {
                'N': self.N,
                'T': self.T,
                'M': self.M,
            }
        )
    
    def append(self, sim_configs=None):
        if not isinstance(sim_configs, list):
            sim_configs = config_sim({'N': self.N, 'T': self.T, 'M': self.M})

        self.exp.append_configs(
            sim_configs=sim_configs,
            initial_state=self.initial_state,
            partial_state_update_blocks=self.partial_state_update_blocks,
            env_processes=self.env_processes,
        )

        return self.exp