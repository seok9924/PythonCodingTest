# 중간 값이라는 것은
#왼쪽에서 최대 오른쪽에서는 최소 인 그런 상황
import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")
import sys
import heapq

n = int(sys.stdin.readline())
left = []
right = []
for i in range(n):
    m = int(sys.stdin.readline())

    if len(left) == len(right):
        heapq.heappush(left, -m)
    else:
        heapq.heappush(right, m)


    if right and right[0]< -left[0]:
        leftnode = heapq.heappop(left)
        rightnode= heapq.heappop(right)

        heapq.heappush(left, -rightnode)
        heapq.heappush(right, -leftnode)
    print(-left[0])

# 파이썬 기본 지원 heqp에서 최소 힙 제공 최대 힙은 - 붙여서 만듬
# 따라서 진행시 여러 풀이가 존재하지만 왼쪽에 두고 서로 길이가 같게 하는 식으로 구성했음
# 완쪽 최대힙의 경우 길이가 같거나 +1 까지 허용   왼/중/오 에서 왼중을 담당
# 만약 진행과정에서 왼의 최대 값이 오보다 크다? 바꿔줘야함


