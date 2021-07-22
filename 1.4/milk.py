"""
ID: 
LANG: PYTHON3
TASK: milk
"""

lst = []
total = 0

with open('milk.in', 'r') as f:
    num, n = map(int, f.readline().strip().split())

    for _ in range(n):
        lst.append(tuple(map(int, f.readline().strip().split())))

lst.sort(key = lambda tup: tup[0])

for cost, amount in lst:
    if num >= amount:
        num -= amount
        total += cost * amount
    else:
        total += cost * num
        break

with open('milk.out', 'w') as f:
    f.write(f'{total}\n')
    f.close()
