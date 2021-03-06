"""
ID: 
LANG: PYTHON3
TASK: transform
"""

def getPattern(f, N):
    p = []
    for i in range(N):
        p.append(fin.readline().strip())
    return p

def rotateClockwise(p, N):
    after = []
    for j in range(N):
        after.append(p[N - 1][j])
    for i in range(N - 1):
        for j in range(N):
            after[j] += p[N - 2 - i][j]
    return after

def verticalReflect(p,N):
    after=[]
    for line in p:
        if N%2==1:
            after.append(line[::-1])
        else:
            after.append(line[int(N/2):N][::-1]+line[0:int(N/2)][::-1])
    return after
fin = open('transform.in','r')
N = int(fin.readline().strip())
before=getPattern(fin,N)
after=getPattern(fin,N)

isSecond=False
temp = before
isRunning=True
while isRunning:
    for rotate in range(3):
        temp=rotateClockwise(temp,N)
        if temp==after:
            if isSecond:
                result = 5
            else:
                result = rotate+1
            isRunning=False
            break
    if not isRunning:
        break
    if isSecond:
        result=7
        break

    temp=before
    temp=verticalReflect(temp,N)
    if temp==after:
        result=4
        break
    isSecond=True
with open('transform.out','w') as fout:
    fout.write(f"{result}\n")
