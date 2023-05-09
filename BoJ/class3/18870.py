import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n=int(input())
numlist=list(map(int,input().split()))
d=dict()

noduplication=list(sorted(set(numlist)))

for i,v in enumerate(noduplication):
    d[v]=i

for number in numlist:
    print(d[number], end=' ')