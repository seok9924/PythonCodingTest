import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n = int(input())
ans = abs(100 - n)
m = int(input())
if m:
    broken = set(input().split())
else:
    broken = set()


for i in range(1000001):
    for j in str(i):
        if j in broken:
            break
    else:
        ans = min(ans, len(str(i)) + abs(i - n))

print(ans)