import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n,m = map(int,input().split())
board=[]
total=[]

for i in range(n):
    board.append(input())



for i in range(n-7):
    for j in range(m-7):
        blackstart=0
        whitestart=0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y)%2 ==0:
                    if board[x][y]!='B':
                        blackstart+=1
                    if board[x][y]!='W':
                        whitestart+=1
                else:
                    if board[x][y]!='W':
                        blackstart+=1
                    if board[x][y]!="B":
                        whitestart+=1
        total.append(blackstart)
        total.append(whitestart)
print(min(total))


