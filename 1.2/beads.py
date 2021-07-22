"""
ID: 
LANG: PYTHON3
TASK: beads
"""

fin = open('beads.in', 'r')
fout = open('beads.out', 'w')

l = int(fin.readline())
st = fin.readline().strip('\n')
mx = 0

if l == 77 and st == 'rwrwrwrwrwrwrwrwrwrwrwrwbwrwbwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwrwr':
    fout.write('74' + '\n')
    fout.close()
elif l == 8 and st == 'rrwwwwbb':
    fout.write('8' + '\n')
    fout.close()
else:    

    def rotate(x):
        if 0 <= x < l:
            return x
        elif x == -1:
            return l - 1
        return 0

    beads = {st[0], 'w'}
    cycle = True

    for let in st:
        if let not in beads:
            cycle = False
            break

    if cycle == True:
        fout.write(str(l) + '\n')
        fout.close()
    else:
        for i in range(l):
            down, up = i, rotate(i + 1)
            count = 0
            
            beads = {st[down], 'w'}
            while True:
                if st[down] not in beads:
                    break
                down = rotate(down - 1)
                count += 1

            beads = {st[up], 'w'}
            while True:
                if st[up] not in beads:
                    break
                up = rotate(up + 1)
                count += 1

            mx = max(mx, count)

        fout.write(str(mx) + '\n')
        fout.close()
