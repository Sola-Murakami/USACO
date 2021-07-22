"""
ID: solasky1
LANG: PYTHON3
TASK: numtri
"""

with open('numtri.in', 'r') as f:
    tri = []
    n = int(f.readline().strip())

    for _ in range(n):
        tri.append(list(map(int, f.readline().strip().split())))

prev_tri = tri[0][:]

for i in range(1, len(tri)):
    tri[i][0] += prev_tri[0]
    tri[i][-1] += prev_tri[-1]
    
    for j in range(1, len(prev_tri)):
        tri[i][j] += max(prev_tri[j - 1], prev_tri[j])

    prev_tri = tri[i][:]

with open('numtri.out', 'w') as f:
    f.write(f'{max(tri[-1])}\n')
    f.close()
