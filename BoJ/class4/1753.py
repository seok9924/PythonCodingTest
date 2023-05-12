import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


import heapq
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,cur=heapq.heappop(q)
        if distance[cur]<dist:
            continue

        for next in graph[cur]:
            nv,nw=next[0],next[1]
            cost=nw+dist

            if cost<distance[nv]:
                distance[nv]=cost
                heapq.heappush(q,(cost,nv))



v,e =map(int,input().split())

start=int(input())
INF=int(1e9)
distance=[INF]*(v+1)
graph=[[] for _ in range(v+1)]
for i in range(e):
    u,v,w= map(int,input().split()) # u to v weight
    graph[u].append((v,w))

dijkstra(start)

for i in range(1,len(distance)):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])