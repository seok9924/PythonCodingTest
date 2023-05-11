import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(n):
    nodes = list(map(int, input().split()))
    for node in range(1, len(nodes) - 2, 2):
        graph[nodes[0]].append((nodes[node], nodes[node + 1]))

def bfs(start):
    que = deque()
    que.append(start)
    total = [0, 0]
    visited = [-1] * (n + 1)
    visited[start] = 0

    while que:
        cur = que.popleft()
        for v, d in graph[cur]:
            if visited[v] == -1:
                visited[v] = visited[cur] + d
                que.append(v)
                if total[0] < visited[v]:
                    total= visited[v], v

    return total


distance, node = bfs(1)
distance, node = bfs(node)
print(distance)