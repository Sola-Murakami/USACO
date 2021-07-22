"""
ID: 
LANG: PYTHON3
TASK: palsquare
"""

with open('palsquare.in', 'r') as f:
    base = int(f.readline().strip())

fout = open('palsquare.out', 'w')

d = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
     6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
     11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
     16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K'}

def baseN(n, base):
    st = ''

    while n > 0:
        st += d[n % base]
        n //= base

    return st[::-1]

def isPal(st):
    return st == st[::-1]

for num in range(1, 301):
    if isPal(baseN(num ** 2, base)):
        fout.write(f'{baseN(num, base)} {baseN(num ** 2, base)}\n')

fout.close()
