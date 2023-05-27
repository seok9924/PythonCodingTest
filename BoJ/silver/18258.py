from collections import deque
import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n = int(input())

q = deque([])

for _ in range(n):
    ok = input().split()
    if ok[0] == 'push':
            q.append(ok[1])
    elif ok[0] == 'pop':
        if len(q):
            print(q.popleft())
        else:
            print(-1)
    elif ok[0] == 'size':
        print(len(q))
    elif ok[0] == 'empty':
        if len(q):
            print(0)
        else:
            print(1)
    elif ok[0] == 'front':
        if len(q):
            print(q[0])
        else:
            print(-1)
    elif ok[0] == 'back':
        if len(q):
            print(q[-1])
        else:
            print(-1)