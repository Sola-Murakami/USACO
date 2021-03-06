"""
ID: 
LANG: PYTHON3
TASK: milk3
"""

def getKey(s):
    n1, n2 = map(int, s.strip().split(" "))
    return n2

fin = open('milk3.in','r')
a,b,c = map(int, fin.readline().split(" "))
result = {*()}
cList = [a, b, c]
mList = [0, 0, c]
result = {*()}
temp=[]

def bucketC(mList):
    for i, p in enumerate(mList):
        for j, q in enumerate(mList):
            if i != j:
                t = mList[:]
                
                if cList[j] - q >= p:
                    t[j] = q + p
                    t[i] = 0
                else:
                    t[i] = p-(cList[j]-q)
                    t[j] = cList[j]
                
                if not t[-1] in result and not t in temp:
                    if t[0] == 0:
                        result.add(t[-1])
                    
                    temp.append(t)
                    bucketC(t)

bucketC(mList)
result = sorted(result)
            
with open('milk3.out','w') as fout:
    out=''
    
    for e in result:
        out+=f'{e} '
    
    fout.write(out.strip()+"\n")
