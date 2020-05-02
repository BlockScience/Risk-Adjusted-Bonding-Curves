import numpy as np

def kappa(R, S, V, I, C, alpha):
    #if bond/burn
    if deltaR != 0:
        kappa = (numpy.log(V0*R))/(numpy.log(S))
    #if attest
    else
        kappa = I/(I-C*alpha)
    return kappa

def invariant_V(R, S, kappa):
    return (S**kappa)/R

def invariant_I(R, C, alpha):
    return R+(C*alpha)
    
def reserve(S, V, kappa):
    return (S**kappa)/V

def supply(R, V, kappa):
    return (V*R)**(1/kappa)

def spot_alpha(I, C, kappa):
    return I*(kappa-1)/(C*kappa)