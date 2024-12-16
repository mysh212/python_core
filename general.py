import os, shutil
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ls = os.listdir
cd = os.chdir
md = os.mkdir
cp = shutil.copyfile
exist = os.path.exists
pwd = os.getcwd
# cd('..')
root = pwd()

def road(i,j):
    if type(i) == 'list':
        ans = root
        for j in i:
           ans = ans + '/' + j
        return ans
    ans = root
    if i: ans = ans + '/' + i
    if j: ans = ans + '/' + j
    return ans

def getfilename(x: str):
    return x.split('/')[::-1][0]

def mkdir(x: str):
    try:
        md(x)
    except:
        warning(f'While making dir {x}')
        return False
    return True

def zt(x,n):
    x = str(x)
    while len(x) < n: x = '0' + x;
    return x

def warning(x: str,pre = None, end = '\n'):
    p = ''
    if pre:
        p = '[' + '] ['.join(pre) + '] '
    print(f'{bcolors.BOLD}{bcolors.WARNING}WARN{bcolors.ENDC} {p}{x}', end = end)
    return

def error(x: str, pre = None, end = '\n'):
    p = ''
    if pre:
        p = '[' + '] ['.join(pre) + '] '
    print(f'{bcolors.BOLD}{bcolors.FAIL}ERROR{bcolors.ENDC} {p}{x}', end = end)
    return

def info(x: str,pre = None, end = '\n'):
    p = ''
    if pre:
        p = '[' + '] ['.join(pre) + '] '
    print(f'{bcolors.BOLD}{bcolors.OKCYAN}INFO{bcolors.ENDC}  {p}{x}', end = end)
    return

def debug(x: str, pre = None, end = '\n'):
    p = ''
    if pre:
        p = '[' + '] ['.join(pre) + '] '
    print(f'{bcolors.BOLD}{bcolors.OKGREEN}DEBUG{bcolors.ENDC} {p}{x}', end = end)
    return

def read_from_file(name: str) -> str:
	f = open(name,'r', encoding = 'UTF-8')
	ans = f.read()
	f.close()
	return ans

def write_to_file(name: str,x):
	with open(name,'w', encoding = 'UTF-8') as f:
		f.write(str(x))
	f.close()
	return

def append_to_file(name: str,x):
	with open(name,'a', encoding = 'UTF-8') as f:
		f.write(str(x))
	return
