"""
ID: solasky1
LANG: PYTHON3
TASK: preface
"""

d = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
count = {'M': 0, 'D': 0, 'C': 0, 'L': 0, 'X': 0, 'V': 0, 'I': 0}

def int_roman(num):
    for k, v in d.items():
        if len(v) == 2:
            count[v[0]] += num // k
            count[v[1]] += num // k
        else:
            count[v] += num // k
        num %= k

with open('preface.in') as f:
    n = int(f.readline().strip())

for num in range(1, n + 1):
    int_roman(num)

with open('preface.out', 'w') as f:
    for let in reversed(count):
        if count[let] != 0:
            f.write(f'{let} {count[let]}\n')
