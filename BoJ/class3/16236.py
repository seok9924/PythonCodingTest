import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import  deque
n=int(input())
graph=[list(map(int,input().split()))for _ in range(3)]
print(graph)

x,y,size=0,0,2
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            x,y=i,j

def eat(x,y,size):
    q=deque()
    visted=[[0]*n for _ in range(n)]
    distance=[[0]*n for _ in range(n)]
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    q.append((x,y))
    visted[x][y]=1
    temp=[]
    while q:
        curx,cury=q.popleft()

        for i in range(4):
            nx=curx+dx[i]
            ny=cury+dy[i]
            if 0<=nx<n and 0<=ny<n and visted[nx][ny]==0:
                if graph[nx][ny]<=size:
                    q.append((nx,ny))
                    visted[nx][ny]=1
                    distance[nx][ny]=distance[curx][cury]+1

                if graph[nx][ny]!=0 and graph[nx][ny]<size:
                    temp.append((nx,ny,distance[nx][ny]))

    return sorted(temp,key=lambda x:(-x[2],-x[0],-x[1]))



result=0

while True:
    shark=eat(x,y,size)
    if len(shark)==0:
        break

    nx,ny,dist=shark.pop()
    result+=dist
    graph[x][y],graph[nx][ny]=0,0
    x,y=nx,ny
    time+=1
    if time==size:
        size+=1
        time=0

print(result)


