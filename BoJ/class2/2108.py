import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


from collections import defaultdict
choibin=defaultdict(int)
n=int(input())
data=[]
for i in range(n):
    data.append(int(input()))

data.sort()

for d in data:
    choibin[d]+=1

outputsave=[]
outputsave.append(round(sum(data)/n))
outputsave.append(data[n//2])
avalue=[]

for i,v in choibin.items():
    if max(choibin.values())==v:
        avalue.append(i)

if len(avalue)>=2:
    choi=avalue[1]
else:
    choi=avalue[0]


outputsave.append(choi)
outputsave.append(abs(data[0]-data[-1]))

for i in outputsave:
    print(i)
