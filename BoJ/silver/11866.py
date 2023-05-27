import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n,k = map(int,input().split())
onelist=[x for x in range(1,n+1)]
deleted=[]

idx=0
for i in range(n):
    idx+=(k-1)
    if idx>=len(onelist):
        idx= idx%len(onelist)
    deleted.append(onelist[idx])
    del onelist[idx]
s='<'
for i in range(n):
    if i<n-1:
        s+=str(deleted[i])+', '
    else:
        s+=str(deleted[i])
s+='>'
print(s)



