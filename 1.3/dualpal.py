"""
ID: 
LANG: PYTHON3
TASK: dualpal
"""
d = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5',
     6: '6', 7: '7', 8: '8', 9: '9', 10: 'A',
     11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F',
     16: 'G', 17: 'H', 18: 'I', 19: 'J', 20: 'K'}

def baseN(n, base):
    st = ''

    while n > 0:
        st += d[n % base]
        n //= base

    return st

def isPal(st):
    return st == st[::-1]

with open('dualpal.in', 'r') as f:
    n, s = map(int, f.readline().strip().split())
    s += 1

fout = open('dualpal.out', 'w')

while n > 0:
    pal_count = 0
    
    for base in range(2, 11):
        if isPal(baseN(s, base)):
            pal_count += 1

            if pal_count == 2:
                fout.write(f'{s}\n')
                n -= 1
                break

    s += 1

fout.close()
