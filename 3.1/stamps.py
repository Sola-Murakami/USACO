"""
ID: solasky1
LANG: PYTHON3
TASK: stamps
"""
with open('stamps.in') as f:
    K, _ = map(int, f.readline().strip().split())
    stamps = [int(num) for st in f.readlines() for num in st.strip().split()]
    dp = [0]
    num = 1

while True:
    mi = float('Inf')
    
    for stamp in stamps:
        if num >= stamp:
            mi = min(mi, dp[num - stamp] + 1)

    if mi > K:
        break
    
    dp.append(mi)
    num += 1

with open('stamps.out', 'w') as f:
    f.write(f'{num - 1}\n')
