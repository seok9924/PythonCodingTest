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
            print(heapq.heappop(listheap)[-1])
    else:
        heapq.heappush(listheap,(abs(oper),oper))


n=int(input())
numbers=[int(input()) for _ in range(n)]
absheap=[]


for number in numbers:
    heap(absheap,number)


