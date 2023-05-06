import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import deque





n= int(input())
meeting=[]
for i in range(n):
    s,e=map(int,input().split())
    meeting.append((s,e))
meeting = sorted(meeting, key=lambda a: (a[1],a[0]))

last = 0
conut = 0
print(meeting)

for i, j in meeting:
  if i >= last:
    conut += 1
    last = j

print(conut)