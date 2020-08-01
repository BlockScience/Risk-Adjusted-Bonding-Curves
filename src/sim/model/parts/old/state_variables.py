# NOT USING THIS ATM
# Everything below is currently in config.py
# initial conditions are sometimes referred to as genesis state

from .sys_params import params

KAPPA = [2]
PRICE = [1]
C = [700]
ALPHA = [0.5, 1]
MONEY_RAISED = [1000]

reserve = MONEY_RAISED[0] - C[0]
supply = KAPPA[0]*(reserve/price)
supply_free = supply
invariant_V = (supply**KAPPA[0])/reserve
invariant_I = reserve + (C*ALPHA[0])

# Put this in sys_params.py
params = {
    'starting_kappa': KAPPA,  # initial kappa
    'starting_alpha': ALPHA,  # initial alpha
    # 'starting_price': price,
    'money_raised': MONEY_RAISED,  # R+C
    'C': C
}

# Put this in state_vars.py
initial_conditions = {
    'reserve': reserve,
    'pbar': price,  # kappa*(reserve/supply), price is dR/dS = 1
    'realized_price': 0,
    'kappa': 0,  # direct to initial kappa in params?
    'supply': supply,
    # 'price': kappa*(reserve/supply), ### kappa*(reserve/supply)
    'alpha': 0,  # direct to initial alpha in params?
    'supply_0': 0,
    'supply_1': 0,
    'supply_free': supply_free,
    'attestations_0': 0,
    'attestations_1': 0,
    'invariant_V': invariant_V,  # (supply**kappa)/reserve
    # (reserve + C*alpha) if alpha is directed to the initial alpha in params, this will change
    'invariant_I': invariant_I
}


'''
initial_conditions = {
    'reserve': 0,
    'supply': 0, 
    'price': kappa*(reserve/supply), ### kappa*(reserve/supply)
    'kappa': 0, ### direct to initial kappa in params?
    'alpha': 0, ### direct to initial alpha in params?
    'supply_0': 0,
    'supply_1': 0,
    'supply_free': supply,
    'attestations_0': 0,
    'attestations_1': 0,
    'invariant_V': 0, ### (supply**kappa)/reserve
    'invariant_I': 0 ### (reserve + C*alpha) if alpha is directed to the initial alpha in params, this will change
} '''


'''
initial_conditions = {'reserve': R0,
                      'supply': S0,
                      'price': P0,
                      'spot_price': P0,
                      'alpha': alpha0,
                      'spot_alpha': alpha0,
                      'rho': rho0
                      }'''
