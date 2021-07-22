"""
ID: solasky1
LANG: PYTHON3
TASK: friday
"""

fin = open('friday.in', 'r')
fout = open('friday.out', 'w')

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = 2
thirteens = [0 for _ in range(7)]

def leap(year):
    if year % 400 == 0:
        return 1
    if year % 100 == 0:
        return 0
    if year % 4 == 0:
        return 1
    return 0

for year in range(1900, 1900 + int(fin.readline())):
    if leap(year):
        months[1] += 1

    month = 0
    day = 0

    for _ in range(365 + leap(year)):
        if day == 12:
            print(month, day_of_week, year)
            thirteens[day_of_week] += 1
            
        day_of_week += 1
        day_of_week %= 7
        day += 1
        if day == months[month]:
            month += 1
            day = 0

    if leap(year):
        months[1] -= 1

fout.write(' '.join([str(num) for num in thirteens]) + '\n')
fout.close()
            
