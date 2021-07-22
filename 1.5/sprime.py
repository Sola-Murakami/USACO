"""
ID: 
LANG: PYTHON3
TASK: sprime
"""

def isPrime(n):
    if n <= 1:
        return False
    if 0 in (n % 2, n % 3):
        if n in (2, 3):
            return True
        return False
    
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0:
            return False
    
    for i in range(7, int(n ** 0.5) + 1, 6):
        if n % i == 0:
            return False
 
    return True

def add(num):
    lst = []
    
    for dig in range(1, 10):
        n = 10 * num + dig

        if isPrime(n):
            lst.append(n)

    return lst

with open('sprime.in') as f:
    n = int(f.readline().strip())

ans = [2, 3, 5, 7]

for _ in range(n - 1):
    new_ans = []
    for x in ans:
        new_ans.extend(add(x))
    ans = new_ans

with open('sprime.out', 'w') as f:
    for st in ans:
        f.write(f'{st}\n')
