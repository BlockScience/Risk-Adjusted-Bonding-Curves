### initial conditions are sometimes referred to as genesis state

from .sys_params import params

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
}


'''
initial_conditions = {'reserve': R0,
                      'supply': S0,
                      'price': P0,
                      'spot_price': P0,
                      'alpha': alpha0,
                      'spot_alpha': alpha0,
                      'rho': rho0
                      }'''
 