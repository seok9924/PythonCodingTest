import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import deque

V,E,S= map(int,input().split())
graph=[[] for i in range(V+1)]
visiteddfs = [False]*(V+1)

for i in range(E):
    v,e=map(int,input().split())
    graph[v].append(e)
    graph[e].append(v)

def bfs(graph,start):
    visted=[False]*(len(graph)+1)
    visted[start]=True
    q=deque()
    q.append(start)
    while q:
        cur=q.popleft()
        print(cur, end=' ')
        graph[cur].sort()
        for vertex in graph[cur]:
            if visted[vertex]!=True:
                visted[vertex]=True
                q.append(vertex)

def dfs(graph,start):
    visiteddfs[start]=True
    print(start,end=' ')
    graph[start].sort()
    for i in graph[start]:
        if not visiteddfs[i]:
            dfs(graph,i)
dfs(graph,start=S)
print()
bfs(graph,start=S)




