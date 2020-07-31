import itertools


E = 0.45  # to be reviewed

KAPPA = [2]

C = [2000]
ALPHA = [0.5]
MONEY_RAISED = [1000]
PERIOD = [2000]

# New price singal : Determines signal shape for agent's behaviour heuristic on price
# rules_price = ["martin"] #, "step"]  # , "ramp", "sin"]

rules_price = ["martin", "step"]  # , "ramp", "sin"]
# rules_price = ["martin", "step", "ramp", "sin"]



# reserve = 300 # MONEY_RAISED[0] - C[0]
# supply = 600 #KAPPA[0]*(reserve/PRICE)
# supply_free = supply
# invariant_V = 1200 #(supply**KAPPA[0])/reserve
# invariant_I = 650 #reserve + (C[0]*ALPHA[0])



print()
# print(type(MONEY_RAISED))
# print(MONEY_RAISED)
# print()

# E = [0.1, 0.2, 0.3]
E = [0.2]

factors = [rules_price, KAPPA, E, MONEY_RAISED, ALPHA, C]
product = list(itertools.product(*factors))
rules_price, KAPPA, E, MONEY_RAISED, ALPHA, C = zip(*product)
rules_price = list(rules_price)
KAPPA = list(KAPPA)
E = list(E)
MONEY_RAISED = list(MONEY_RAISED)
ALPHA = list(ALPHA)
C = list(C)

# Put this in sys_params.py
params = {
    'starting_kappa': KAPPA,  # initial kappa
    'starting_alpha': ALPHA,  # initial alpha
    # 'starting_price': price,
    'money_raised': MONEY_RAISED,  # reserve + C
    'C': C,  # Commited outcome payout
    'f': [0.03],  # param to control certainty of alpha at extremes
    'm': [0.15],  # param to modulate curvature of alpha threshold band
    'beta': [0.9],
    'dust': [10**(-8)],
    'period': PERIOD,
    'rules_price': rules_price,
    'E': E
}