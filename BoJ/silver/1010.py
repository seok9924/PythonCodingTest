import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

t=int(input())

def factorial(n):
    if n in d:
        return d[n]
    else:
        d[n]= d[n-1]*n
d={0:1,1:1}

for i in range(2,31):
    factorial(i)


for i in range(t):
    east,west=map(int,input().split())
    print(factorial(west)//(factorial(west-east)*factorial(east)))
