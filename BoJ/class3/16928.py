import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n,m=map(int,input().split())

from collections import deque
ladder={}
snake={}
for i in range(n):
    a,b=map(int,input().split())
    ladder[a]=b

for i in range(m):
    a,b=map(int,input().split())
    snake[a]=b
visited=[0]*101
countdice=[0]*101
def bfs(start):
    q=deque()
    q.append(start)
    step=7

    while q:
        cur=q.popleft()
        if cur==100:
            print(countdice[cur])
            break
        for i in range(1,step):
            next=cur+i

            if next<=100 and not visited[next]:
                if next in ladder:
                    next=ladder[next]
                if next in snake:
                    next=snake[next]

                if not visited[next]:
                    visited[next]=1
                    countdice[next]=countdice[cur]+1

                    q.append(next)
bfs(1)
