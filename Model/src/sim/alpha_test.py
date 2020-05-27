# RUN
# The following imports NEED to be in the exact order
import numpy as np
from copy import deepcopy
from cadCAD.configuration.utils import config_sim
from cadCAD.configuration import append_configs
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
import config
from cadCAD import configs
import pandas as pd


def run(drop_midsteps=True):
    exec_mode = ExecutionMode()
    multi_proc_ctx = ExecutionContext(context=exec_mode.multi_proc)
    run = Executor(exec_context=multi_proc_ctx, configs=configs)
    results = pd.DataFrame()
    i = 0
    for raw_result, _ in run.execute():
        params = configs[i].sim_config['M']
        result_record = pd.DataFrame.from_records(
            [tuple([i for i in params.values()])], columns=list(params.keys()))

        df = pd.DataFrame(raw_result)
        # keep only last substep of each timestep
        if drop_midsteps:
            max_substep = max(df.substep)
            is_droppable = (df.substep != max_substep) & (df.substep != 0)
            df.drop(df[is_droppable].index, inplace=True)

        result_record['dataset'] = [df]
        results = results.append(result_record)
        i += 1
    return results.reset_index()

# STATE VAR UPDATE: PRIVATE ALPHA


def update_private_alpha(params, substep, state_history, prev_state, policy_input):
    # Private alpha belief signal is a ramp
    # sign = (-1)**int((2*prev_state['timestep']/signal['period']))
    # new_private_alpha = prev_state['alpha'] + signal['dP']*sign
    new_private_alpha = P0[0] + signal['dP'] * \
        np.sin(2*np.pi*prev_state['timestep']/signal['period'])
    # plt.plot(new_private_alpha, substep)
    # plt.show()
    print("new_private_alpha = ", new_private_alpha)
    return 'private_alpha', new_private_alpha

# POLICY: SET ACTION


def set_action(params, substep, state_history, prev_state):
    private_alpha = prev_state['private_alpha']
    start_alpha = params['starting_alpha']
    alpha = prev_state['alpha']
    s = prev_state['agent_supply']

    if alpha > private_alpha:
        mech = 'attest_neg'
        print("Agent attests negative. alpha = ",
              alpha, "private_alpha = ", private_alpha)
        amt_Q1 = 0
        amt_Q0 = alpha - private_alpha  # units
        amt_neg = amt_Q0  # VERIFY THIS # units
        amt_pos = 0
        S0 = S0 + amt_neg
        Q0 = Q0 + amt_Q0

    elif alpha < private_alpha:
        mech = 'attest_pos'
        print("Agent attests positive. alpha = ",
              alpha, "private_alpha = ", private_alpha)
        amt_Q1 = private_alpha - alpha  # units
        amt_Q0 = 0
        amt_neg = 0
        amt_pos = amt_Q1  # VERIFY THIS
        S1 = S1 + amt_pos
        Q1 = Q1 + amt_Q1

    else:
        # don't attest
        mech = None
        amt_Q1 = 0
        amt_Q0 = 0
        amt_pos = 0
        amt_neg = 0
        print("No attestation. alpha = ", alpha,
              "private_alpha = ", private_alpha)

    return {
        'mech': mech,
        'amt_Q1': amt_Q1,
        'amt_Q0': amt_Q0,
        'amt_pos': amt_pos,
        'amt_neg': amt_neg
    }

# STATE VAR UPDATE: ALPHA


def update_alpha(params, substep, state_history, prev_state, policy_input):

    alpha = prev_state['alpha']
    E = 1.3
    R = 300
    C = 700
    Q1 = [1]
    q1 = [0]
    S1 = [1]
    S0 = [0]
    s1 = [0]
    s = [20]
    deltaq1 = [1]  # deltaq1 = deltas
    deltas = [1, 4, 5, 6, 3, 2, 0, 4]

    for i in range(len(deltas)):
        A = (1/(Q1[i]*(Q1[i]+deltaq1[i]))) * \
            ((q1[i]*(Q1[i]*deltas[i]) - (deltaq1[i]*s[i])) +
             deltaq1[i]*((Q1[i]*s1[i]) + (Q1[i]*deltas[i])))

        alpha_bar = (deltas[i]*R)/(A*(C+R) - (deltas[i]*C))

        new_alpha = E*(alpha[i]) + (1-E)*(alpha[i])*((S1[i]+S0[i])/(S1[i]+S0[i]+deltas[i])) + \
            (alpha_bar)*(deltas[i]/(S1[i]+S0[i]+deltas[i]))

    print("A = ", A)
    print("alpha_bar = ", alpha_bar)
    print("new_alpha = ", new_alpha)

    # Update operations
    Q1.append(Q1[i] + deltaq1[i])
    S1.append(S1[i] + deltas[i])
    S0.append(S0[i])
    s1.append(s1[i] + deltas[i])
    s.append(s[i] - deltas[i])
    q1.append(q1[i] + deltaq1[i])
    alpha.append(new_alpha)
    deltaq1.append(deltas[i])


# PSUBS
partial_state_update_blocks = [
    {
        'policies': {
            'act': set_action
        },
        'variables': {
            'private_alpha': update_private_alpha
        }
    },
    {
        'policies': {
            'act': set_action
        },
        'variables': {
            'alpha': update_alpha
            # 'agent_supply': update_s
        }
    }
]

# CONFIG.PY
time_periods_per_run = 400
monte_carlo_runs = 1

ALPHA = [0.5]
C = [700]
Q1 = 1
Q0 = 1

reserve = 300
invariant_I = reserve + (C[0]*ALPHA[0])

# params
params = {
    'starting_alpha': ALPHA,  # initial alpha
}

# initial conditions
initial_conditions = {
    'private_alpha': 0,
    'alpha': ALPHA,
    'supply_0': 0,
    'supply_1': 0,
    'attestations_0': Q0,
    'attestations_1': Q1,
    'invariant_I': invariant_I,
    'agent_attestations_1': 0,
    'agent_attestations_0': 0,
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
    sim_configs=sim_config  # dict containing simulation parameters
)

for c in configs:
    c.initial_state = deepcopy(c.initial_state)

    print("Params (config.py) : ", c.sim_config['M'])

    c.initial_state['alpha'] = c.sim_config['M']['starting_alpha']

