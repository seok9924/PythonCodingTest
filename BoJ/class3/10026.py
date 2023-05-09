import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


from collections import deque
n=int(input())
picture=[]
colorweak=[]

for i in range(n):
    picture.append(input())

for i in range(n):
    s=''
    for j in range(n):
        if picture[i][j] =="G":
            s+='R'
            continue
        s+=picture[i][j]
    colorweak.append(s)

visited = [[0] * n for _ in range(n)]
weakvisited=[[0] * n for _ in range(n)]

def bfs(x,y,pic_or_weak,visited):
    q=deque()
    q.append((x,y))
    visited[x][y]=1
    color=pic_or_weak[x][y]
    dx=[0,0,-1,1]
    dy=[1,-1,0,0]

    while q:
        curx,cury=q.popleft()

        for i in range(4):
            nx=curx+dx[i]
            ny=cury+dy[i]


            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if color==pic_or_weak[nx][ny]:
                    visited[nx][ny]=1
                    q.append((nx,ny))

    return 1

total=0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            total+=bfs(i,j,picture,visited)

weaktotal=0
for i in range(n):
    for j in range(n):
        if not weakvisited[i][j]:
            weaktotal+=bfs(i,j,colorweak,weakvisited)
print(total,weaktotal)