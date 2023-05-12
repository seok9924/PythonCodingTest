import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n= int(input())
m=int(input())
graph=[[] for _ in range(n+1)]

for i in range(m):
    s,e,w=map(int,input().split())
    graph[s].append((e,w))

start,end=map(int,input().split())

import heapq
INF=int(1e9)
distance=[INF]*(n+1)
def dijkstra(start):
    distance[start]=0
    q=[]
    heapq.heappush(q,(0,start))

    while q:
        dist,cur=heapq.heappop(q)

        if distance[cur]<dist:
            continue
        for next in graph[cur]:

            cost=next[1]+dist
            if cost<distance[next[0]]:
                distance[next[0]]=cost
                heapq.heappush(q,(cost,next[0]))
dijkstra(start)
print(distance[end])
