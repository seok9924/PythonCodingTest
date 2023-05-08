import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

    # D n=2n if 결과 n>9999 n=n%10000
    # S n=n-1 if n=0 => n=9999
    # L 왼쪽 shift
    # R 오른쪽 shift

from collections import  deque
def d_oper(n):
    n*=2
    if n>9999:
        n%=10000

    return n
def s_oper(n):
    if n==0:
        n=9999
        return n
    else:
        n-=1
        return n
def l_oper(n):
    first= n%1000
    last=n//1000
    return first*10+last

def r_oper(n):
    first = n%10
    last = n//10
    return first*1000+last


def bfs(a,b):
    q=deque()
    visted=set()
    q.append((a,""))
    visted.add(a)
    while q:
        cur_num,oper=q.popleft()
        if cur_num==b:
            print(oper)
            return
        check= d_oper(cur_num)
        if check not in visted:
            visted.add(check)
            q.append((check,oper+"D"))



        check= s_oper(cur_num)

        if check not in visted:
            visted.add(check)
            q.append((check,oper+"S"))

        check= l_oper(cur_num)

        if check not in visted:
            visted.add(check)
            q.append((check,oper+"L"))

        check= r_oper(cur_num)

        if check not in visted:
            visted.add(check)
            q.append((check,oper+"R"))
t=int(input())
for i in range(t):
    A,B= map(int,input().split())
    bfs(A,B)

