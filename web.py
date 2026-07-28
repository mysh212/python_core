# Author : ysh
# 2025/11/17 Mon 17:37:45
from core.general import *
import core.log as log

from datetime import datetime
from collections import defaultdict

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

class damper:
    def __init__(self):
        self.f = defaultdict(lambda: defaultdict(float))
        pass

    def access(self, IP: str, name: str = '', delay: int = 0):
        now = datetime.now().timestamp()
        pre = self.f[name][IP]
        if abs(now - pre) < delay:
            return False
        self.f[name][IP] = now
        return True

    def clear(self):
        self.f.clear()
        return

damp = damper()

def require(request, f: list, delay: int = 0, name: str = '') -> bool:
    if not damp.access(request.remote_addr, name, delay):
        return False
    for i in f:
        if i not in request.values:
            return False
    return [request.values[i] for i in f]