import sys
from os import path
from collections import deque

if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n,m = map(int, input().split())

graph=[]

for i in range(n):
    graph.append(list(map(int,input())))


def findcount(graph):
    queue=deque()
    queue.append((0,0))
    dx=[1,1,0,0]
    dy=[0,0,-1,1]
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            if graph[nx][ny]==0:
                continue
            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(findcount(graph))