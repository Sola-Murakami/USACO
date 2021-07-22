"""
ID: 
LANG: PYTHON3
TASK: frac1
"""

import math

with open('frac1.in') as f:
    n = int(f.readline().strip())

fracs = {*()}

for denom in range(1, n + 1):
    for numer in range(0, denom + 1):
        gcd = math.gcd(numer, denom)
        fracs.add((numer // gcd, denom // gcd))

with open('frac1.out', 'w') as f:
    fracs = sorted(fracs, key = lambda frac: frac[0] / frac[1])

    for frac in fracs:
        f.write(f'{frac[0]}/{frac[1]}\n')
