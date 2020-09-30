import pandas as pd

from cadCAD.engine import ExecutionMode, ExecutionContext, Executor
from cadCAD.configuration import Experiment
from cadCAD import configs

def run(drop_midsteps: bool=True) -> pd.DataFrame:

    def get_M(k, v):
        if k == 'sim_config':
            k, v = 'M', v['M']
        return k, v


    config_ids = [
        dict(
            get_M(k, v) for k, v in config.__dict__.items() if k in ['simulation_id', 'run_id', 'sim_config', 'subset_id']
        ) for config in configs
    ]

    exec_mode = ExecutionMode()
    exec_context = ExecutionContext(exec_mode.local_mode)
    run = Executor(exec_context=exec_context, configs=configs)
    # results = pd.DataFrame()

    (system_events, tensor_field, sessions) = run.execute()

    df = pd.DataFrame(system_events)
    for i, config_id in enumerate(config_ids):
        params = config_id['M']
        result_record = pd.DataFrame.from_records([tuple([i for i in params.values()])], columns=list(params.keys()))
        sub_df = df[df.subset == config_id['subset_id']]

    if drop_midsteps:
        max_substep = max(df.substep)
        is_droppable = (df.substep != max_substep)
        is_droppable &= (df.substep != 0)
        df = df.loc[~is_droppable]

    result_record['dataset'] = [sub_df]
    df = df.append(result_record)

    return (df.reset_index(), tensor_field, sessions)

# if __name__ == '__main__':
#     import sys
#     # check
#     sys.path.append('./src')

#     from config_wrapper import ConfigWrapper
#     # import options as options

#     # change 
#     import model as model
    
#     config = ConfigWrapper(market_model)
#     config.append()

#     results = run(drop_midsteps=True)
#     print(results)