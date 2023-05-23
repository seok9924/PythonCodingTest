import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")



from itertools import combinations
n,m=map(int,input().split())

chicken=[]

for i in range(n):
    chicken.append(list(map(int,input().split())))

nchicken=0
location=[]
house=[]
for i in range(n):
    for j in range(n):
        if chicken[i][j]==2:
            nchicken+=1
            location.append([i,j])
        if chicken[i][j]==1:
            house.append([i,j])
chickencombi=list(combinations(location,m))

total=[]
for combi in chickencombi:
    distance=[]
    for ho in house:
        hx,hy= ho
        cdd=int(1e9)
        for co in combi:
            cx,cy=co
            cd=abs(hx-cx)+abs(hy-cy)
            cdd=min(cd,cdd)
        distance.append(cdd)
    total.append(sum(distance))
print(min(total))