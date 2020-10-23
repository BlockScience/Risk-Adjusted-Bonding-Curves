import itertools

KAPPA = [2] # computed from I / I-(C*alpha)

C = [72000] #some amount greater than money raised, some ROI (10%) over money raised
ALPHA = [0.03536977491961415] # computed using S1 * reserve / (S1 * reserve - S0 * reserve + S0*C[0])
MONEY_RAISED = [66000]
PERIOD = [1200]

### Monthly instalment from Impact Investor
monthly_instalment = [3000]

# New price singal : Determines signal shape for agent's behaviour heuristic on price
# rules_price = ["martin"] #, "step"]  # , "ramp", "sin"]

rules_price = ["martin"]  # , "ramp", "sin"]
# rules_price = ["martin", "step", "ramp", "sin"]


# reserve = 300 # MONEY_RAISED[0] - C[0]
# supply = 600 #KAPPA[0]*(reserve/PRICE)
# supply_free = supply
# invariant_V = 1200 #(supply**KAPPA[0])/reserve
# invariant_I = 650 #reserve + (C[0]*ALPHA[0])

####### CONTINUOUS FUNDING #####################
ENABLE_CONTINUOUS = [False]
THETA = [0.9]  # PORTION OF FUNDS FROM BONDING TO PROJECT, (1-theta) to reserve
####### CONTINUOUS FUNDING #####################

####### BURN ACTION #####################
ENABLE_BURN = [False]
####### BURN ACTION #####################

####### UNSIWAP STYLE TRADING #####################
fee_numerator = [997]
fee_denominator = [1000]

####### UNSIWAP STYLE TRADING #####################

#Alpha and price should be biased similarly
# -1 indicates negative bias, signal linearly decreasing
# 1 indicates positive bias, signal linearly increasing
alpha_bias = [-1]
price_bias = [-1]

print()

# E = [0.1, 0.2, 0.3]
E = [0.2]

factors = [rules_price, KAPPA, E, MONEY_RAISED, ALPHA, C, THETA, ENABLE_CONTINUOUS, ENABLE_BURN, alpha_bias, price_bias]
product = list(itertools.product(*factors))
rules_price, KAPPA, E, MONEY_RAISED, ALPHA, C, THETA, ENABLE_CONTINUOUS, ENABLE_BURN, alpha_bias, price_bias= zip(*product)
rules_price = list(rules_price)
KAPPA = list(KAPPA)
E = list(E)
MONEY_RAISED = list(MONEY_RAISED)
ALPHA = list(ALPHA)
C = list(C)
THETA = list(THETA)
ENABLE_CONTINUOUS = list(ENABLE_CONTINUOUS)
ENABLE_BURN = list(ENABLE_BURN)
alpha_bias = list(alpha_bias)
price_bias = list(price_bias)

########## SYSTEM PARAMETERS ##########
params = {
    'starting_kappa': KAPPA,  # initial kappa
    'starting_alpha': ALPHA,  # initial alpha
    'money_raised': MONEY_RAISED,  # reserve + C
    'monthly_instalment': monthly_instalment,
    'C': C,  # Commited outcome payout
    'f': [0.03],  # param to control certainty of alpha at extremes
    'm': [0.15],  # param to modulate curvature of alpha threshold band
    'beta': [0.9],  # param for Armijo rule
    'dust': [10**(-8)],  # param for Armijo rule
    'period': PERIOD,
    'rules_price': rules_price,
    'E': E,
    'ENABLE_CONTINUOUS' : ENABLE_CONTINUOUS,
    'THETA' : THETA,
    'ENABLE_BURN' : ENABLE_BURN,
    'fee_numerator' : fee_numerator,
    'fee_denominator' : fee_denominator,
    'alpha_bias': alpha_bias,
    'price_bias': price_bias,

}
