import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

k,n = map(int,input().split())
a=[]

for _ in range(k):
    a.append(int(input()))
start=1
end=max(a)
while start<=end:
    mid=(start+end)//2
    total=0
    for element in a:
        total+=element//mid

    if total>=n:
        start=mid+1
    else:
        end=mid-1
print(end)