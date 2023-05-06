import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import deque
check_list=[]
n=int(input())
house=[[0]*n for _ in range(n)]
for i in range(n):
    a=input()
    for j in range(n):
        house[i][j]=int(a[j])
def bfs(x,y):
    count = 1
    q=deque()
    q.append((x,y))
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    house[x][y]=0

    while q:
        curx,cury=q.popleft()

        for i in range(4):
            nx=curx+dx[i]
            ny=cury+dy[i]

            if nx<0 or ny<0 or nx>=n or ny>=n:
                continue
            if house[nx][ny]==1:
                q.append((nx,ny))
                count+=1
                house[nx][ny]=0
    return count


danji=[]
for i in range(n):
    for j in range(n):
        if house[i][j]==1:
            danji.append(bfs(i,j))

danji.sort()
print(len(danji))
for i in danji:
    print(i)