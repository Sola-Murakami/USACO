"""
ID: 
LANG: PYTHON3
TASK: gift1
"""

fin = open('gift1.in', 'r')
fout = open('gift1.out', 'w')

d = dict()
order = list()

for _ in range(int(fin.readline())):
    inp = fin.readline()
    d[inp] = 0
    order.append(inp)

while True:
    giving = fin.readline()
    money, ppl = map(int, fin.readline().split())
    if ppl == 0:
        continue
    give, keep = divmod(money, ppl)
    d[giving] += keep - money
    
    for _ in range(ppl):
        d[fin.readline()] += give

for name in order:
    fout.write(name + ' ' + str(d[name]) + '\n')

fout.close()


