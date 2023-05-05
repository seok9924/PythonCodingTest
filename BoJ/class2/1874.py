import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n = int(input())
stack = []
plus_minus=''
cur = 1
checkpoint=True
for i in range(n):
    a=int(input())
    while cur<=a:
        stack.append(cur)
        cur+=1
        plus_minus+='+'
    if stack[-1]==a:
        stack.pop()
        plus_minus+='-'

    else:
        print("NO")
        checkpoint=False
        break

if checkpoint:
    for i in plus_minus:
        print(i)