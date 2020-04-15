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
            'attestations_pos': update_Q1,
            'attestations_neg': update_Q0,
            'spot_price': update_P,
            'output_price': update_Pbar,
            'price': capture_Pin,
            'spot_alpha': update_alpha,
            'output_alpha': update_alphabar,
            'alpha': capture_alpha,  
            'kappa': update_kappa
        }
    }
]