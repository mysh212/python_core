# Author : ysh
# 2025/11/17 Mon 17:37:45
from core.general import *
import core.log as log

info = warning = lambda *x, **y: None

def ok(data = None, custom: bool = False, **ot) -> dict:
    if len(ot) == 0:
        return {
            'ok': True,
            'data': data
        } if data is not None else {
            'ok': True
        }
    if data is not None:
        ot['data'] = data
    # info('OK detected, returning ' + str({
    #     'ok': True,
    #     'data': ot
    # } if not custom else {
    #     'ok': True,
    #     'data': data,
    #     **ot
    # }))
    return {
        'ok': True,
        'data': ot
    } if not custom else {
        'ok': True,
        'data': data,
        **ot
    }

def fail(error = None) -> dict:
    # warning('Error detected, returning ' + str({
    #     'ok': False,
    #     'data': error,
    #     'error': error
    # }))
    return {
        'ok': False,
        'data': error,
        'error': error
    }

def require(request, f: list) -> bool:
    for i in f:
        if i not in request.values:
            return False
    return True