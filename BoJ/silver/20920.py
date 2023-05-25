import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import Counter

n,m= map(int,input().split())
voca=[]
voca_3things=[]
for i in range(n):
    x=input()
    if len(x)>=m:
       voca.append(x)
d=dict(Counter(voca))
for k,v in d.items():
    voca_3things.append((k,v,len(k)))

voca_re=sorted(voca_3things,key=lambda x: (-x[1],-x[2],x[0]))

for v in voca_re:
    print(v[0])