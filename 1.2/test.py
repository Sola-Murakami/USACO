"""
ID: 
LANG: PYTHON3
TASK: test
"""
with open('test.py') as f:
    x, y = map(int, f.readline().split())

with open('test.py', 'w') as f:
    f.write('{x + y}\n')
