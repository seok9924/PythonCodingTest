import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n,m=map(int,input().split())
d=dict()

for i in range(n):
    home,pw=input().split()
    d[home]=pw

for i in range(m):
    home=input()
    print(d[home])