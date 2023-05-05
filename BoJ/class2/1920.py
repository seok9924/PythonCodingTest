import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import defaultdict

n=int(input())
A=list(map(int,input().split()))
m=int(input())
B=list(map(int,input().split()))

check=defaultdict(int)

for a in A:
    check[a]+=1

for b in B:
    if b in check:
        print('1')
    else:
        print('0')

