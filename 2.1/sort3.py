"""
ID: solasky1
LANG: PYTHON3
TASK: sort3
"""

with open('sort3.in', 'r') as f:
    n = int(f.readline())
    c1, c2, c3 = 0, 0, 0
    swaps = 0
    have = []

    for _ in range(n):
        num = int(f.readline().strip())
        have.append(num)

        if num == 1:
            c1 += 1
        elif num == 2:
            c2 += 1
        else:
            c3 += 1

    want = [1 for _ in range(c1)] + [2 for _ in range(c2)] + [3 for _ in range(c3)]

for i in range(n):
    for j in range(n):
        if have[i] != want[i] and have[j] != want[j]:
            if have[i] == want[j] and have[j] == want[i]:
                have[i] = want[i]
                have[j] = want[j]
                swaps += 1
        
nbad = 0

for i in range(n):
    if have[i] != want[i]:
        nbad += 1

swaps += nbad // 3 * 2

with open('sort3.out', 'w') as f:
    f.write(f'{swaps}\n')
