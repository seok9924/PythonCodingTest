import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


import heapq
def heap(listheap,oper):
    if oper==0 :
        if len(listheap)==0:
            print(0)
        else:
            print(-heapq.heappop(listheap))


    else:

        heapq.heappush(listheap,oper)

n= int(input())
data=[int(input()) for _ in range(n)]

heaps=[]
for d in data:
    heap(heaps,oper=-d)