"""
ID: solasky1
LANG: PYTHON3
TASK: pprime
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

with open('pprime.in') as f:
    r_min, r_max = map(int, f.readline().strip().split())

prime_pals = []

for num in (5, 7, 11):
    prime_pals.append(num)

for x in range(1, 10):
    for y in range(10):
        num = 101 * x + 10 * y
        
        if isPrime(num):
            prime_pals.append(num)

for x in range(1, 10):
    for y in range(10):
        for z in range(10):
            num = 10001 * x + 1010 * y + 100 * z

            if isPrime(num):
                prime_pals.append(num)

for w in range(1, 10):
    for x in range(10):
        for y in range(10):
            for z in range(10):
                num = 1000001 * w + 100010 * x + 10100 * y + 1000 * z

                if isPrime(num):
                    prime_pals.append(num)

with open('pprime.out', 'w') as f:
    for prime in prime_pals:
        if r_min <= prime <= r_max:
            f.write(f'{prime}\n')
