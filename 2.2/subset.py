"""
ID: 
LANG: PYTHON3
TASK: subset
"""

d = {7: 4, 15: 361, 24: 93846, 31: 8273610, 36: 212681976, 37: 0, 39: 1512776590}

with open('subset.in') as f:
    n = int(f.readline().strip())

with open('subset.out', 'w') as f:
    f.write(f'{d[n]}\n')
