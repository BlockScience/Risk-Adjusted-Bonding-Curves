# The following imports NEED to be in the exact order

from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from src.sim import config as sys_model
from cadCAD import configs
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)


def run(drop_midsteps=True):
    exec_mode = ExecutionMode()
    local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)
    runner = Executor(exec_context=local_mode_ctx, configs=configs)
    #results = pd.DataFrame()

    # pprint(configs)

    raw_system_events, tensor_field, sessions = runner.execute()
    simulation_result = pd.DataFrame(raw_system_events)
    print(type(simulation_result))
    print(tensor_field)
    print()
    return simulation_result.reset_index()

# print(simulation_result)
# print(f"Tensor Field: {type(tensor_field)}")
# print(tabulate(tensor_field, headers='keys', tablefmt='psql'))
# print(f"Output: {type(simulation_result)}")
# print(tabulate(simulation_result, headers='keys', tablefmt='psql'))
# print()

# i = 0
# verbose = False
# results = {}
# for raw_result, tensor_field in run.execute():
#     result = pd.DataFrame(raw_result)
#     if verbose:
#         print()
#         print(f"Tensor Field: {type(tensor_field)}")
#         print(tabulate(tensor_field, headers='keys', tablefmt='psql'))
#         print(f"Output: {type(result)}")
#         print(tabulate(result, headers='keys', tablefmt='psql'))
#         print()
#     results[i] = {}
#     results[i]['result'] = result
#     results[i]['simulation_parameters'] = simulation_parameters[i]
#     i += 1
