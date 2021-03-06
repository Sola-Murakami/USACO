"""
ID: 
LANG: PYTHON3
TASK: barn1
"""

fin = open('barn1.in','r')
m, s, c = map(int,fin.readline().strip().split())
if m>=c:
    total=c
else:
    barnList = list(filter(None,fin.read().split('\n')))
    barnList = [int(n) for n in barnList]
    barnList.sort()
    start=end = barnList[0]
    
    bList=[]
    i=0
    for i in range(1,c-1):
        if barnList[i]-end==1:
            end=barnList[i]
        else:
            bList.append(end-start+1)

            bList.append(barnList[i]-end)
            start=end=barnList[i]
    else:
        bList.append(end-start+1)
        bList.append(barnList[i+1]-end)
        bList.append(1)

    while True:    
        min=9999
        t=0

        for i in range(2,len(bList),2):
            result=0
            for j in range(0,len(bList),2):
                if 0<i-j<=2:
                    continue
                elif i==j:
                    result+=bList[i-2]+bList[i-1]+bList[i]-1
                else:
                    result+=bList[j]

            if result<=min:
                min=result
                t=i
        
        tempList=[]
        for j in range(len(bList)):
                if 0<t-j<=2:
                    continue
                elif t==j:
                    tempList.append(bList[t-2]+bList[t-1]+bList[t]-1)
                else:
                    tempList.append(bList[j])
        bList=tempList        
        
        if int((len(bList)+1)/2)==m:
            total=min
            break
            
with open('barn1.out','w') as fout:
    fout.write(f"{total}\n")
