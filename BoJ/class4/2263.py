import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n=int(input())
inoder=list(map(int,input().split()))
postoder=list(map(int,input().split()))

root=postoder[-1]

print(root)