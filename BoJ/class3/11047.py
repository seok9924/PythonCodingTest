import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n,k= map(int,(input().split()))

coins=[int(input()) for _ in range(n)]

total=0
while True:
    tmp=[]
    idxs=[]
    for idx,coin in enumerate(coins):
        if k//coin!=0:
          tmp.append(k//coin)
          idxs.append(idx)

    total+=min(tmp)
    if k%coins[idxs[-1]]==0:
        break
    k=k-coins[idxs[-1]]*min(tmp)

print(total)

