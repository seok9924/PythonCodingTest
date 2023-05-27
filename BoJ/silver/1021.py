import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import deque
n,m= map(int,input().split())
xlist=list(map(int,input().split()))
q=deque([i for i in range(1,n+1)])
count=0
for x in xlist:
    while True:
        if q[0]==x:
            q.popleft()
            break
        else:
            if q.index(x)<len(q)/2:
                while q[0]!=x:
                    q.append(q.popleft())
                    count+=1
            else:
                while q[0]!=x:
                    q.appendleft(q.pop())
                    count+=1
print(count)




