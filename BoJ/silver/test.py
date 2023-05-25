import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n = int(input())
a = list(map(int, input().split()))
a_max = max(a)
a_min = min(a)
print(a_max * a_min)