# Author : ysh
# 2026/02/11 Wed 19:58:41
import core.general
from core.general import exist, mkdir, write_to_file, append_to_file
from datetime import datetime
import os, json

def _log(name = None, _status = None, data = None, ot = {}, _file = None):
    if len(data) == 1: data = data[0];
    else: data = [*data];
    if len(ot) != 0 and data: ot['data'] = data;
    elif data: ot = data

    path = _file or os.getenv('LOG_PATH') or 'general.log'

    try:
        date = datetime.strftime(datetime.now(), '%Y/%m/%d %H:%M:%S.%f')
        pre = f'{_status} | {date} | [{name}] -> {json.dumps(ot)}\n'
        
        if not exist('log'):
            core.general.warning('Log directory does not exist, creating.')
            mkdir('log')

        if not exist(f'log/{path}'):
            core.general.warning('Log file does not exist, creating one.')
            write_to_file(f'log/{path}', '')
        
        append_to_file(f'log/{path}', pre)
        return
    except:
        core.general.error('ERROR occured while logging, ignoring.')
        return

# def info(name = None, *data, **ot):
#     return _log(data = data, name = name, _status = 'INFO ', ot = ot)

# def debug(name = None, *data, **ot):
#     return _log(data = data, name = name, _status = 'DEBUG', ot = ot)

# def warning(name = None, *data, **ot):
#     return _log(data = data, name = name, _status = 'WARN ', ot = ot)

# def error(name = None, *data, **ot):
#     return _log(data = data, name = name, _status = 'ERROR', ot = ot)

def info(name = None, filename = None):
    return lambda *data, **ot: _log(data = data, name = name, _status = 'INFO ', ot = ot, _file = filename)

def debug(name = None, filename = None):
    return lambda *data, **ot: _log(data = data, name = name, _status = 'DEBUG', ot = ot, _file = filename)

def warning(name = None, filename = None):
    return lambda *data, **ot: _log(data = data, name = name, _status = 'WARN ', ot = ot, _file = filename)

def error(name = None, filename = None):
    return lambda *data, **ot: _log(data = data, name = name, _status = 'ERROR', ot = ot, _file = filename)