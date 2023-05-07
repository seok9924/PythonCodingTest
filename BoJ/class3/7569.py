import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import deque
m,n,h= map(int,input().split())
q=deque()
tomato = []
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,input().split())))
        for k in range(m):
            if tmp[j][k]==1:
                q.append([i,j,k])
    tomato.append(tmp)


def bfs(q):

    dx=[0,0,0,0,-1,1]
    dy=[0,0,-1,1,0,0]
    dz=[1,-1,0,0,0,0]

    while q:
        curx,cury,curz=q.popleft()
        for i in range(6):
            nx=curx+dx[i]
            ny=cury+dy[i]
            nz=curz+dz[i]

            if nx<0 or nx>=h or ny<0 or ny>=n or nz<0 or nz>=m:
                continue

            if tomato[nx][ny][nz]==0:
                tomato[nx][ny][nz]=tomato[curx][cury][curz]+1

                q.append((nx,ny,nz))

day =0
bfs(q)
for i in tomato:
    for j in i :
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day=max(day,max(j))
print(day-1)

