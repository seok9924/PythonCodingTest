import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n,m= map(int,input().split())
data=list(map(int,input().split()))
partial=[0]
tmp=0
for d in data:
    tmp+=d
    partial.append(tmp)
for i in range(m):
     x,y=map(int,input().split())
     print(partial[y]-partial[x-1])