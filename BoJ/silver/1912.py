import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")
import sys
input=sys.stdin.readline
n=int(input())

a=list(map(int,input().split()))
d={0:a[0]}
for i in range(1,n):
    d[i]=max(d[i-1]+a[i],a[i])
print(max(d.values()))