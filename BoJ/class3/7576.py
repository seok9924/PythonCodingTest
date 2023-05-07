import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import deque
m,n= map(int,input().split())
q=deque()
tomato = []
for i in range(n):
    tomato.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if tomato[i][j]==1:
            q.append((i,j))


def bfs(q):

    dx=[0,0,-1,1]
    dy=[-1,1,0,0]

    while q:
        curx,cury=q.popleft()
        for i in range(4):
            nx=curx+dx[i]
            ny=cury+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=m :
                continue

            if tomato[nx][ny]==0:
                tomato[nx][ny]=tomato[curx][cury]+1

                q.append((nx,ny))

day =0
bfs(q)
for i in tomato:
    for j in i :
        if j==0:
            print(-1)
            exit(0)
    day=max(day,max(i))
print(day-1)
