# The following imports NEED to be in the exact order
from cadCAD import configs
# ADD FOR PRINTING CONFIG
from cadCAD.configuration.utils import *
from cadCAD.engine import ExecutionMode, ExecutionContext, Executor

from src.sim import config

exec_mode = ExecutionMode()
exec_ctx = ExecutionContext(context=exec_mode.multi_proc)
simulation = Executor(exec_context=exec_ctx, configs=configs)
raw_system_events, tensor_field, session = simulation.execute()
df = pd.DataFrame(raw_system_events)


def get_M(k, v):
    if k == 'sim_config':
        k, v = 'M', v['M']
    return k, v


config_ids = [
    dict(
        get_M(k, v) for k, v in config.__dict__.items() if k in ['simulation_id', 'run_id', 'sim_config', 'subset_id']
    ) for config in configs
]


    # 4.18 Method MC
def run(drop_midsteps=True, df = df):
    # results = df
    print('config_ids = ', config_ids)
    # sub_dfs = pd.DataFrame(columns= range(max(df.subset)+1))
    
    results = pd.DataFrame()
    for i, config_id in enumerate(config_ids):
        params = config_id['M']
        result_record = pd.DataFrame.from_records([tuple([i for i in params.values()])], columns=list(params.keys()))
        sub_df = df[df.subset == config_id['subset_id']]
        # sub_df = df[df.subset == config_id['subset_id']][df.run == config_id['run_id'] + 1]

        # print(sub_df.head())
        if drop_midsteps:
            max_substep = max(sub_df.substep)
            is_droppable = (sub_df.substep != max_substep) & (sub_df.substep != 0)
            sub_df.drop(sub_df[is_droppable].index, inplace=True)


        # subset_id = max(sub_df.subset)
        # print(max(df.subset))
        # # sub_dfs = pd.DataFrame()
        # # if max(sub_df.subset) ==  
        # sub_dfs[subset_id].append(sub_df, ignore_index=True)
        # sub_dfs[subset_id].append(sub_df[subset_id])
        # sub_dfs[subset_id] = pd.concat(sub_dfs[subset_id])
        

        result_record['dataset'] = [sub_df]
        results = results.append(result_record)

    return results.reset_index()
