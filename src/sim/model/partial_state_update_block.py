# One Timestep can contain multiple PSUBs
# At the end of each PSUB (called a substep), cadCAD returns the state of the system

from src.sim.model.parts.private_beliefs import *
from src.sim.model.parts.bondburn import *
from src.sim.model.parts.attest import *
from src.sim.model.parts.choose_action import set_action
from src.sim.model.parts.monthly_instalment import add_instalment
from src.sim.model.parts.choose_agent import choose_agent
from src.sim.model.parts.put_agent_back_to_df import put_agent_back_to_df

# print("-----------------PSUB---------------------")

partial_state_update_block = [
    {
        'policies': {
            # 'agent': choose_agent
        },
        'variables': {
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # Initialization and exogenous processes
            'chosen_agent': choose_agent,
            #'public_alpha': update_public_alpha
        }
    },
    {
        'policies': {
             # 'act': set_action
         },
        'variables': {
             # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
             # Agent signaling
             # Capture any private signals eg. sine wave
             #'agent_private_price': update_private_price,
             #'agent_private_alpha': update_private_alpha,
             'chosen_agent': update_agent_beliefs
         }
    },
    {
        'policies': {
            'act': set_action,
            'add_instalment': add_instalment,
        },
        'variables': {
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # Bond-to-mint or burn-to-withdraw
            'reserve': update_R,
            'supply': update_S,
            'spot_price': update_P_bondburn,
            'pbar': update_pbar,
            'invariant_I': update_I_bondburn,
            'chosen_agent': update_agent_BC
        }
    },
    {
        'policies': {
            'act': set_action
        },
        'variables': {
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # Attest positive or attest negative
            'attestations': update_Q,
            'attestations_1': update_Q1,
            'attestations_0': update_Q0,
            'supply_1': update_S1,
            'supply_0': update_S0,
            'supply_free': update_S_free,
            'chosen_agent': update_agent_PM,
            'alpha': update_alpha,
            'kappa': update_kappa,
            'spot_price': update_P_attest,
            'invariant_V': update_V
        }
    },
    # {
    #     'policies': {
    #     },
    #     'variables': {
    #         # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
    #         # Resolve metrics

    #     }
    # },
    {
        'policies': {

        },
        'variables': {
            # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
            # Close out
            'agents': put_agent_back_to_df
        }
    }
]
