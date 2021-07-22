"""
ID: 
LANG: PYTHON3
TASK: combo
"""

with open('combo.in', 'r') as f:
    n = int(f.readline().strip())
    combs = []

    for _ in range(2):
        combs.append(list(map(int, f.readline().strip().split())))

s = set()

def combine(lst1, lst2):
    lst3 = []
    
    for x in range(len(lst1)):
        lst3.append((lst1[x] + lst2[x]) % n)

    return tuple(lst3)

for comb in combs:
    for err1 in range(-2, 3):
        for err2 in range(-2, 3):
            for err3 in range(-2, 3):
                lst = [err1, err2, err3]
                
                s.add(combine(comb, lst))

with open('combo.out', 'w') as f:
    f.write(f'{len(s)}\n')
    f.close()
