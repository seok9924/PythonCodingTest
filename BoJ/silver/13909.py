import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

import math

n=int(input())
count=0
for i in range(1,n+1):
    case=i**2
    if case<(n+1):
        count+=1
    else:
        break

print(count)