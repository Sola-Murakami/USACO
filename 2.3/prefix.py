"""
ID: solasky1
LANG: PYTHON3
TASK: prefix
"""

with open('prefix.in') as f:
    prims = []
    s = []
    
    while True:
        line = f.readline().strip()
        if line == '.':
            break
        
        prims.extend(line.split())
    
    while True:
        line = f.readline().strip()
        if not line:
            break
        s.append(line)

    s = ''.join(s)

d = [False] * len(s)

for i in range(len(s)):
    for w in prims:
        if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or i-len(w) == -1):
            d[i] = True

with open('prefix.out', 'w') as f:
    boo = False
    
    for i in reversed(range(len(d))):
        if d[i]:
            boo = True
            f.write(f'{i+1}\n')
            break

    if not boo:
        f.write('0\n')
    
    
            
