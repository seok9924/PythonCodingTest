import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import defaultdict
t=int(input())

for i in range(t):
    n=int(input())
    d=defaultdict(int)
    all_wear=[input() for _ in range(n)]
    for wear in all_wear:
        d[wear.split()[-1]]+=1
    count=1
    for k,v in d.items():
        count*=v+1
    print(count-1)
