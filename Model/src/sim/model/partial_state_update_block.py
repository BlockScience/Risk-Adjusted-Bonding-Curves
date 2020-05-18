# One Timestep can contain multiple PSUBs
# At the end of each PSUB (called a substep), cadCAD returns the state of the system

from .parts.initialization import *
from .parts.private_beliefs import *
from .parts.choose_action import *
from .parts.bondburn import *
from .parts.attest import *

partial_state_update_blocks = [
    {
        'policies': {
        },
        'variables': {
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # Initialization and exogenous processes # skip for now

        }
    },
    {
        'policies': {
            'act': set_action
        },
        'variables': {
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # Agent signaling
            # Capture any private signals eg. sine wave
            'private_price': update_private_price,
            'private_alpha': update_private_alpha
        }
    },
    {
        'policies': {
            'act': set_action
        },
        'variables': {
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # Bond-to-mint or burn-to-withdraw
            'reserve': update_R,
            'supply': update_S,
            'agent_reserve': update_r,
            'agent_supply': update_s_bondburn,
            'spot_price': update_P_bondburn,  # verify
            'price': update_pbar,  # verify
            'invariant_I': update_I
        }
    },
    {
        'policies': {
            'act': set_action
        },
        'variables': {
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # Attest positive or attest negative
            'supply_1': update_S1,
            'supply_0': update_S0,
            'agent_supply': update_s_attest,
            'agent_supply_1': update_s1,
            'agent_supply_0': update_s0,
            'attestations_1': update_Q1,
            'attestations_0': update_Q0,
            'agent_attestations_1': update_q1,
            'agent_attestations_0': update_q0,
            'alpha': update_alpha,
            'kappa': update_kappa,
            'spot_price': update_P_attest,
            'invariant_V': update_V
        }
    },
    {
        'policies': {
        },
        'variables': {
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # Resolve metrics

        }
    },
    {
        'policies': {
        },
        'variables': {
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # Close out

        }
    }
]


'''
partial_state_update_blocks = [
    {
      'policies': {
          'act': set_action,
        },
        'variables': {
            'reserve': update_R, 
            'supply': update_S,
            'supply_1': update_S1,
            'supply_0': update_S0,
            'attestations_1': update_Q1,
            'attestations_0': update_Q0,
            'spot_price': update_P,
            'output_price': update_Pbar,
            'price': capture_Pin,
            'spot_alpha': update_alpha,
            'output_alpha': update_alphabar,
            'alpha': capture_alpha,  
            'kappa': update_kappa
        }
    }
] '''
