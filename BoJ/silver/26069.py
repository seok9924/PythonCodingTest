import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


from collections import  defaultdict

n=int(input())
d=defaultdict(int)
d['ChongChong']=1
for i in range(n):
    a,b=input().split()

    if a in d or b in d:
        d[a]=1
        d[b]=1

print(len(d.values()))
