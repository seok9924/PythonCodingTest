import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

t=int(input())

for i in range(t):
    x,y=map(int,input().split())
    distance=y-x
    count=0
    k=1
    while distance>0:
        distance-=k
        count+=1
        if distance:
            distance-=k
            count+=1
        else:
            break
        k+=1
    print(count)