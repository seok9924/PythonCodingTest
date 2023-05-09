import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n=int(input())
d={1:1,2:2}
def dp(x):
    if x in d:
        return d[x]
    else:
        d[x]=dp(x-1)+dp(x-2)
        return d[x]

print(dp(n)%10007)


