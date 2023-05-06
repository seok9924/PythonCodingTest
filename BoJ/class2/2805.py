import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n,m = map(int, input().split())
trees=list(map(int,input().split()))



def treecut(h):
    total=0
    for tree in trees:
        if tree>h:
            total+=tree-h
    return total

start=1
end=max(trees)
while start<=end:
    mid=(start+end)//2

    total=treecut(mid)
    if total>=m:
        start=mid+1

    else:
        end=mid-1
print(end)
