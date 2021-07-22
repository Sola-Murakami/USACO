"""
ID: 
LANG: PYTHON3
TASK: milk2
"""

fin = open('milk2.in', 'r')
fout = open('milk2.out', 'w')

n = int(fin.readline())
lst = []

for _ in range(n):
    lst.append([int(x) for x in fin.readline().split()])

lst.sort()

max_cont = 0
l = len(lst)
i, j = 0, 0

while j < l:
    a, b = lst[i], lst[j]
    
    if a[1] >= b[0]:
        max_cont = max(max_cont, b[1] - a[0])
        j += 1
    else:
        j += 1
        i = j

max_idle = 0

for i in range(len(lst) - 1):
    max_idle = max(max_idle, lst[i + 1][0] - lst[i][1])

fout.write(str(max_cont) + ' ' + str(max_idle) + '\n')
fout.close()
