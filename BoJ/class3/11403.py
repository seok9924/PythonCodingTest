import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


from collections import deque
def bfs(x):
    q=deque()
    q.append(x)
    visited[x]=1

    while q:
        curx=q.popleft()
        for i in graphdict[curx]:
            if not visited[i]:
                visited[i]=1
                q.append(i)
    









n=int(input())

graph=[list(map(int,input().split())) for _ in range(n)]
graphdict=dict()
for i in range(n):
    graphdict[i]=[]
visited = [0] * n
for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            graphdict[i].append(j)
print(graphdict)
