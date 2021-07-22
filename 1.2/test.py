"""
ID: 
LANG: PYTHON3
TASK: test
"""
with open('test.in') as f:
    x, y = map(int, f.readline().split())

with open('test.out', 'w') as f:
    f.write(f'{x + y}\n')
