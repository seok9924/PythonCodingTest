from collections import deque
n=int(input())

k=[_ for _ in range(1,n+1)]

q=deque(k)

while q:
    q.popleft()
    q.append(q.popleft())

    if len(q)==1:
        print(q[0])
        break

