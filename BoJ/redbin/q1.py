import sys
from os import path


# if path.exists('input.txt'):
#     sys.stdin = open("input.txt", "r")


# input =sys.stdin.readline

n, k = map(int, input().split())

items = [[0,0]]

for i in range(n):
    items.append(list(map(int, input().split())))

dp= [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        if j >= items[i][0]:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-items[i][0]]+items[i][1])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][k])

#이 문제 풀때는 2차원 배열을 만들어서 풀어야 한다.