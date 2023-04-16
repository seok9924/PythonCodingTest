from collections import deque
def bfs(graph,start):
    visited=[start]
    queue=deque(start)

    while queue :
        cur=queue.popleft()
        for i in graph[cur]:
            if i not in visited:
                visited.append(i)
                queue.append(i)

    return visited
