"""
ID: solasky1
TASK: skidesign
LANG: PYTHON3
"""

with open('skidesign.in', 'r') as f:
    n = int(f.readline().strip())
    hills = [int(f.readline().strip()) for _ in range(n)]
    mi = float('Inf')

for i in range(0, 84):
    cost = 0

    for h in hills:
        if h < i:
            cost += (i - h) ** 2
        elif h > i + 17:
            cost += (i + 17 - h) ** 2

    mi = min(mi, cost)

with open('skidesign.out', 'w') as f:
    f.write(f'{mi}\n')
    f.close()
