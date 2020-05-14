import numpy as np

E =  # epsilon for convex combination
C =  # payout commitment


def kappa(R, S, V):
    kappa = (numpy.log(V*R))/(numpy.log(S))
    return kappa


def alpha():


def spot_price():


def spot_alpha():


def alpha_bar():


def invariant_V(R, S, kappa):
    return (S**kappa)/R


def invariant_I(deltaR, R, alpha):
    return I = R+(C*alpha)


def reserve():
    # if last action was bond/burn
    # if last action was attest


def supply(R, V, kappa):
    return (V*R)**(1/kappa)


def supply_0():


def supply_1():


def attestations_1():


def attestations_0():


def bond():


def burn():


def attest_pos():


def attest_neg():
