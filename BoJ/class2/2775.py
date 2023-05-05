import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


t= int(input())





for _ in range(t):
    a=int(input())
    b=int(input())

    data=[_ for _ in range(1,b+1)]
    for i in range(a):
        for j in range(1,b):
            data[j]+=data[j-1]

    print(data[-1])


