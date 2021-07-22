"""
ID: solasky1
LANG: PYTHON3
TASK: ride
"""

fin = open('ride.in', 'r')
fout = open('ride.out', 'w')

def let_to_num(let):
    return ord(let) - 64

def go_or_stay(boo):
    if boo == True:
        return 'GO'
    else:
        return 'STAY'

s = set()

for _ in range(2):
    st = fin.readline()
    num = 1

    for let in st:
        num *= let_to_num(let)
        num %= 47

    s.add(num)

fout.write(go_or_stay(len(s) == 1) + '\n')
fout.close()
