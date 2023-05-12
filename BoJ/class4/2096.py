


import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n = int(input())
data = list(map(int,input().split()))
maxdp = data
mindp = data
for _ in range(n-1):
    a,b,c = map(int,input().split())
    maxdp = [a+max(maxdp[0],maxdp[1]),b+max(maxdp),c+max(maxdp[1],maxdp[2])]
    mindp = [a+min(mindp[0],mindp[1]),b+min(mindp),c+min(mindp[1],mindp[2])]
print(max(maxdp),min(mindp))