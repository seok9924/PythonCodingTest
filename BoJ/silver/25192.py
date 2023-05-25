import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from collections import defaultdict
n= int(input())

chatlist=[input() for _ in range(n)]
d=defaultdict(int)
count=0
for chat in chatlist:
    if chat=='ENTER':
        d=defaultdict(int)
        continue
    if chat not in d:
        d[chat]+=1
        count+=1
print(count)

