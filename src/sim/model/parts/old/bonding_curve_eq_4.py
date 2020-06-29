# import numpy as np
#
# E = #epsilon for convex combination
# C = #payout commitment
#
# def kappa(deltaR, R, S, V, I, alpha):
#     #if bond/burn and attest
#     if deltaR != 0 && deltaAlpha != 0:
#         kappa = ### ???
#     #if only bond/burn
#     elif deltaR != 0:
#         kappa = (numpy.log(V*R))/(numpy.log(S))
#     #if only attest
#     elif deltaAlpha != 0:
#         kappa = I/(I-C*alpha)
#     #if no action
#     else:
#         kappa = (numpy.log(V*R))/(numpy.log(S))
#         ### check if (numpy.log(V*R))/(numpy.log(S)) == I/(I-C*alpha)
#     return kappa
#
# def invariant_V(R, S, kappa):
#     return (S**kappa)/R
#
# def invariant_I(deltaR, R, alpha):
#     #if bond/burn and attest
#     if deltaR != 0 && deltaAlpha != 0:
#         I = R+(C*alpha)
#     #if only bond/burn
#     elif deltaR != 0:
#         I = R+(C*alpha)
#     #if only attest
#     elif deltaAlpha != 0:
#         I = (C*alpha)/(1-(1/kappa))
#         ### check if R+(C*alpha) == (C*alpha)/(1-(1/kappa))
#     #if no action
#     else:
#         I = R+(C*alpha)
#     return I
#
# def reserve(deltaR, S, V, I, alpha, kappa):
#     #if bond/burn and attest
#     if deltaR != 0:
#         R = (S**kappa)/V
#     #if only attest or no action
#     else:
#         R = I - (C*alpha)
#         ### check if (I - C*alpha) == (S**kappa)/V
#     return R
#
# def supply(R, V, kappa):
#     return (V*R)**(1/kappa)
#
# def spot_price(deltaR, deltaS, deltaAlpha, R, S, kappa):
#     #if bond/burn and attest
#     if deltaR != 0 && deltaAlpha != 0:
#         SP = kappa*(R/S)
#     #if only bond/burn
#     elif deltaR != 0:
#         SP = deltaR/deltaS
#     #if only attest
#     elif deltaAlpha != 0:
#         SP = kappa*(R/S)
#     #if no action
#     else:
#         SP = kappa*(R/S)
#     return SP
#
# def spot_alpha(deltaS, R, S1, S0, alpha):
#     #if attest
#     if deltaS != 0:
#         alpha_bar = alpha_bar(deltaS, R, C) ### define alpha_bar
#         SA = E*(alpha) + (1-E)*(alpha)*((S1+S0)/(S1+S0+deltaS)) + (alpha_bar)*(deltaS/(S1+S0+deltaS))
#     #if no attest
#     else:
#         SA = alpha
#     return SA
#
# def alpha_bar(deltas, deltaq1, R, C, Q1, q1, s1, s): ### what about Q0, S0, and attest_negative?
#     A = (1/(Q1*(Q1+deltaq1)))*((q1*(Q1*deltas) - (deltaq1*s)) + deltaq1*((Q1*s1) + (Q1*deltas)))
#     alpha_bar = (deltas*R)/(A*(C+R) - (deltas*C))
#     return alpha_bar
#
# def bond(deltaR, R, S):
#     kappa = ### ???
#     V = invariant_V(R, S, kappa)
#     deltaAlpha = 0
#     deltaS = (V*(R+deltaR))**(1/kappa)-S
#     realized_price = spot_price(deltaR, deltaS, deltaAlpha, R, S, kappa) ### or is it deltaR/deltaS?
#     return deltaS, realized_price
#
# def burn(deltaS, R, S):
#     kappa = ### ???
#     V = (S**(kappa))/R
#     deltaAlpha = 0
#     deltaR = R-((S-deltaS)**kappa)/V
#     realized_price = spot_price(deltaR, deltaS, deltaAlpha, R, S, kappa) ### or is it deltaR/deltaS?
#     return deltaR, realized_price
#
#
#
#
#
#
