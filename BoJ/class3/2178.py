import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import deque
n,m= map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))


dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
        curx,cury=q.popleft()

        for i in range(4):
            nx=curx+dx[i]
            ny=cury+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny] = graph[curx][cury]+1
                q.append((nx,ny))
    return graph[n-1][m-1]


print(bfs(0,0))