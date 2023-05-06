import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n=int(input())
m=int(input())
visited=[False]*(n+1)
graph=[[] for i in range(n+1)]
for i in range(m):
    x,y=map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
def dfs(start):
    visited[start]=True


    for i in graph[start]:
        if not visited[i]:
            dfs(i)
dfs(1)

count=0
for i in visited:
    if i :
       count+=1

print(count-1)