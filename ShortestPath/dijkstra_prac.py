import heapq
n=10
INF=int(1e9)
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

def dijkstra(start):
    q=[]
    distance[start]=0
    heapq.heappush(q,(0,start))

    while q:
        dis,cur=heapq.heappop(q)

        if distance[cur]<dis:
            continue

            for next in graph[cur]:
                cost=dist+next[1]

                if distance[next[0]]>cost:
                    distance[next[0]]=cost
                    heapq.heappush(q,(cost,next[0]))
