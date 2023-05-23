import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n = int(input())
H = list(map(int, input().split()))  # 처음 나무의 길이
A = list(map(int, input().split()))  # 나무들이 자라는 길이
answer = 0
day = n

while day >= 1:
    i = A.index(max(A))
    answer = answer + (A[i] * (day - 1)) + H[i]
    H[i], A[i] = 0, 0
    day -= 1

print(answer)