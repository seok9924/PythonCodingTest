import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n,m=map(int,input().split())
dogam=[0]*(n+1)


for i in range(1,n+1):
    dogam[i]=input()

print()
