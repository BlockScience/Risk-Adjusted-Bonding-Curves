# NOT USING THIS ATM
from action import *


def update_R(params, step, sL, s, _input):

    action = _input['action']
    R = action['posterior']['R']

    key = 'reserve'
    value = R

    return (key, value)
