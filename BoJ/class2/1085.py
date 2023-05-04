import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")



x,y,w,h = map(int,input().split())
print(min(x,y,w-x,h-y))