import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


from collections import deque
n,m=map(int,input().split())

graph=[[] for i in range(n+1)]

for i in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q=deque([start])
    visited[start]=1

    while q:
        traget=q.popleft()

        for i in graph[traget]:
            if not visited[i]:
                visited[i]=visited[traget]+1
                q.append(i)
baconlist=[]


for i in range(1,n+1):
    visited=[0]*(n+1)
    bfs(i)
    baconlist.append(sum(visited))
print(baconlist.index((min(baconlist)))+1)