import random
import math


def add_instalment(params, substep, state_history, prev_state):
    params = params[0]
    monthly_instalment = params['monthly_instalment']
    timestep = prev_state['timestep']

    if timestep%25 == 0:
        monthly_instalment = monthly_instalment
    else:
        monthly_instalment = 0

    return {
        'monthly_instalment': monthly_instalment
    }

