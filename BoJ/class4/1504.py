import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

import heapq

def dijkstra(start):
    distance = [INF] * (n + 1)

    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))
    while q:
        dist,cur= heapq.heappop(q)

        if distance[cur]<dist:
            continue
        for next in graph[cur]:
            cost=next[1]+dist

            if distance[next[0]]>cost:
                distance[next[0]]=cost
                heapq.heappush(q,(cost,next[0]))
    return distance

n,m= map(int,input().split())
graph=[[] for _ in range(n+1)]

for i in range(m):
    a,b,c= map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))



v1,v2=map(int,(input().split()))
INF=int(1e9)

v1v2=dijkstra(1)[v1]+dijkstra(v1)[v2]+dijkstra(v2)[n]
v2v1=dijkstra(1)[v2]+dijkstra(v2)[v1]+dijkstra(v1)[n]

if v1v2 and v2v1 >INF:
    print(-1)
else:
    print(min(v1v2,v2v1))

