"""
ID: solasky1
LANG: PYTHON3
TASK: cowtour
"""

from math import sqrt
INF = float('Inf')

def weight(x, y):
    return sqrt((x[0] - y[0])**2 + (x[1] - y[1])**2)


with open("cowtour.in", "r") as f:
    N = int(f.readline().strip())
    V = []
    for i in range(N):
        V.append(tuple(map(int, f.readline().strip().split())))

    M = [None for _ in range(N)]
    for i in range(N):
        M[i] = [bool(int(x)) for x in f.readline().strip()]

dist = [[INF]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if M[i][j]:
            dist[i][j] = weight(V[i], V[j])

for i in range(N):
    dist[i][i] = 0

for k in range(N):
    for i in range(N):
        for j in range(N):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

max_dist = [0] * N

for i in range(N):
    max_dist[i] = max([x for x in dist[i] if x < INF])

fields = []
s = set()

for i in range(N):
    if i not in s:
        field = set()

        for j in range(N):
            if dist[i][j] < INF:
                field.add(j)
                s.add(j)

        fields.append(field)

dias = [0]*len(fields)
for f in range(len(fields)):
    diam = 0

    for i in fields[f]:
        for j in fields[f]:
            if dist[i][j] > diam:
                diam = dist[i][j]

    dias[f] = diam

res = []

for a in range(len(fields)):
    for b in range(a+1, len(fields)):
        min_dia = INF
        for i in fields[a]:
            for j in fields[b]:
                dia = max(
                    max_dist[i] + max_dist[j] + weight(V[i], V[j]),
                    dias[a],
                    dias[b]
                )

                if min_dia > dia:
                    min_dia = dia

        res.append(min_dia)

with open("cowtour.out", "w") as f:
    f.write("%.6f\n" % min(res))

