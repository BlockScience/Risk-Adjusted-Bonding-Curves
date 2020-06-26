# The following imports NEED to be in the exact order
from pprint import pprint
from Model.src.sim import config as sys_model

from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from cadCAD import configs
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)
import tabulate

exec_mode = ExecutionMode()
local_mode_ctx = ExecutionContext(context=exec_mode.local_mode)
run = Executor(exec_context=local_mode_ctx, configs=configs)

# pprint(configs)

raw_system_events, tensor_field, sessions = run.execute()
simulation_result = pd.DataFrame(raw_system_events)
print(type(simulation_result))
print(tensor_field)
print()

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
