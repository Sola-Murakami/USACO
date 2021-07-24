"""
ID: 
LANG: PYTHON3
TASK: fracdec
"""
def frac_to_dec(numer, denom):
    times = ''
    if numer < 0 and denom > 0 or numer > 0 and denom < 0:
        times = '-'
        numer = abs(numer)
        denom = abs(denom)
    if numer < 0 and denom < 0:
        numer *= -1
        denom *= -1
    
    dec = []
    rems = []
    
    while True:
        dec.append(str(numer // denom))
        numer %= denom
        rems.append(numer)
        numer *= 10
        
        if numer == 0:
            if len(dec) == 1:
                return times + dec[0] + '.0'
            return times + dec[0] + '.' + ''.join(dec[1:])
        
        if rems.count(rems[-1]) > 1:
            dec.insert(rems.index(rems[-1]) + 1, '(')
            dec.append(')')
            return times + dec[0] + '.' + ''.join(dec[1:])

with open('fracdec.in') as f:
    numer, denom = map(int, f.readline().strip().split())

with open('fracdec.out', 'w') as f:
    dec = frac_to_dec(numer, denom)
    f.write(f'{dec}\n')
