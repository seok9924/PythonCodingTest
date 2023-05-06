import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


from collections import deque


def bfs(start):
    q=deque([start])
    while q:
        cur=q.popleft()
        if cur==m:
            return array[cur]
        for next in (cur-1,cur+1,cur*2):
            if 0<=next and next<MAX and not array[next]:
                array[next]=array[cur]+1
                q.append(next)


MAX=100001
n,m=map(int,input().split())
array=[0]*MAX
print(bfs(n))