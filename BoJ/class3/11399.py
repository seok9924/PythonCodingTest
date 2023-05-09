import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

import heapq

n= int(input())
people=list(map(int,(input().split())))

total=0
heapq.heapify(people)
smallest=[]
while people:
    a=heapq.heappop(people)
    total+=a
    smallest.append(total)

print(sum(smallest))


# n= int(input())
# a=list(map(int,input().split()))
# a.sort()
# k=[0]*n
# k[0]=a[0]
# for i in range(1,n):
#     k[i]=k[i-1]+a[i]
# print(sum(k))