# NOT USING THIS ATM
from action import *


def update_S(params, step, sL, s, _input):

    action = _input['action']
    S = action['posterior']['S']

    key = 'supply'
    value = S

    return (key, value)
