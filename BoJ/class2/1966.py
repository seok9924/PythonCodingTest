from collections import deque


import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

def printerqueue(docs,m):
    if len(docs)==1:
        print(1)
    else:
        a=docs.popleft()




import heapq
from collections import deque
t = int(input())

for i in range(t):
    n,m=map(int,input().split())
    q=deque(list(map(int,input().split())))
    idx = deque(list(range(n)))
    cnt = 0

    while q:
        if q[0] == max(q):
            cnt += 1
            q.popleft()
            pop_idx = idx.popleft()
            if pop_idx == m:
                print(cnt)
        else:
            q.append(q.popleft())
            idx.append(idx.popleft())