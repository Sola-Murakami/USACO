"""
ID: solasky1
TASK: wormhole
LANG: PYTHON3
"""

with open('wormhole.in', 'r') as f:
    numholes = int(f.readline().strip())
    holepos = [(0, 0)]

    for _ in range(numholes):
        holepos.append(tuple(map(int, f.readline().strip().split())))
    
partner, nexthole = ([0 for i in range(numholes + 1)] for _ in range(2))

for i in range(1, numholes + 1):
  pos = i
  
  for j in range(1, numholes + 1):
    if holepos[j][0] > holepos[pos][0] and holepos[j][1] == holepos[pos][1]:
      if nexthole[i] == 0 or holepos[j][0] - holepos[i][0] < holepos[nexthole[i]][0]-holepos[i][0]:
        nexthole[i] = j

def solve():
  count = 0
  
  for i in range(1, numholes + 1):
    if partner[i] == 0: 
      break

  if i == numholes:
    for j in range(1, numholes + 1):
      pos = j
      
      for c in range(numholes):
        pos = nexthole[partner[pos]]
    
      if pos != 0:
          return 1
    
    return 0

  for j in range(i + 1, numholes + 1):
    if partner[j] == 0:
      partner[i] = j
      partner[j] = i
      count += solve()
      partner[i] = partner[j] = 0

  return count

with open('wormhole.out', 'w') as f:
    f.write(f'{solve()}\n')
    f.close()
