"""
ID: solasky1
LANG: PYTHON3
TASK: ride
"""
def let_to_num(let):
    return ord(let) - 64

def go_or_stay(boo):
    return 'GO' if boo else 'STAY'

with open('ride.in') as f:
    s = set()
    
    for _ in range(2):
        st = f.readline().strip()
        num = 1

        for let in st:
            num *= let_to_num(let)
            num %= 47

        s.add(num)

with open('ride.out', 'w') as f:
    f.write(f'{go_or_stay(len(s) == 1)}\n')
