"""
ID: 
LANG: PYTHON3
TASK: friday
"""
with open('friday.in') as f:
    n = int(f.readline().strip())

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = 2
thirteens = [0 for _ in range(7)]

def leap(year):
    if not year % 400:
        return 1
    if not year % 100:
        return 0
    if not year % 4:
        return 1
    return 0

for year in range(1900, 1900 + n):
    if leap(year):
        months[1] += 1

    month, day = 0, 0

    for _ in range(365 + leap(year)):
        if day == 12:
            thirteens[day_of_week] += 1
            
        day_of_week += 1
        day_of_week %= 7
        day += 1
        if day == months[month]:
            month += 1
            day = 0

    if leap(year):
        months[1] -= 1

with open('friday.out', 'w') as f:
    ans = " ".join([str(num) for num in thirteens])
    f.write(f'{ans}\n')
