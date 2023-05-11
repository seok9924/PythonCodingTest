import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


def find(x):
    if x!= parent[x]:
        return find(parent[x])
    return x


def union(a,b):
    a=find(a)
    b=find(b)

    if a<b :
        parent[b]=a
    else:
        parent[a]=b


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
_, *t = map(int, input().split())
for i in t:
    parent[i] = 0

partys = []
for _ in range(m):
    p, *q = map(int, input().split())
    partys.append(q)
    if p == 1:
        continue

    # 만난 적 있는 사람들끼리 유니온 파인드
    for i in range(p - 1):
        union(q[i], q[i + 1])

ans = 0
for party in partys:
    for i in party:
        if find(parent[i]) == 0:
            break
    else:
        ans += 1
print(ans)