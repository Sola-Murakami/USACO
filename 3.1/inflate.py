"""
ID: solasky1
LANG: PYTHON3
TASK: inflate
"""
with open('inflate.in') as f:
    M, _N = map(int, f.readline().strip().split())
    cats = [tuple(map(int, line.strip().split())) for line in f]
    dp = [0] * (M + 1)

for i in range(M + 1):
    for points, time in cats:
        if i >= time:
            dp[i] = max(dp[i], dp[i - time] + points)

with open('inflate.out', 'w') as f:
    f.write(f'{dp[-1]}\n')
