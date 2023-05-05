import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

import math
n=int(input())
numbers=list(map(int,input().split()))
count=0
for i in numbers:
    position=True
    if i==1:
        continue
    else:
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                position=False
                continue
        if position:
            count+=1
print(count)