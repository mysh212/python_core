# Author : ysh
# 2025/11/17 Mon 17:37:45
from core.general import *
import core.log as log

from datetime import datetime
from collections import defaultdict

from typing import Any

info = warning = lambda *x, **y: None

# class switch:
#     def __init__(self, x: bool = False):
#         self.x = x

#     def pull(self):
#         self.x = True

#     def push(self):
#         self.x = False

#     def __bool__(self):
#         return self.x

#     def __str__(self):
#         return f'<A switch with value {self.x}>'

class result:
    def __init__(self, ans: bool, block: bool, block_types: bool, data = None):
        self.ans = ans
        self.block = block
        self.block_types = block_types
        self.data = data

    def __bool__(self):
        return self.ans

    def __str__(self):
        return f'<Response in core.web with result {self.ans} & {self.block}>'

    def __iter__(self):
        for i in self.data:
            yield i
        return

# block = switch()

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

def require(request, f: list, delay: int = 0, name: str = '', types: list[type] | None = None) -> bool:
    if not damp.access(request.remote_addr, name, delay):
        return result(False, True, False)
    for i in f:
        if i not in request.values:
            return result(False, False, False)
    if types is not None:
        assert(len(f) == len(types))
        ans = []
        for i, tp in zip(f, types):
            if tp is Any:
                ans.append(i)
                continue
            try:
                ans.append(tp(request.values[i]))
            except:
                return result(False, False, True)
        return ans
    return result(True, False, False, [request.values[i] for i in f])