import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n=int(input())

d={1:1,2:3}


def dp(n):

    if n in d:
        return d[n]

    else:
        d[n]=dp(n-1)+2*dp(n-2)

        return d[n]


print(dp(n)%10007)