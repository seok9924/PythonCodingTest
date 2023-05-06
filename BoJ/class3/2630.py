import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")


n=int(input())

data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
white,blue=0,0

def division(x,y,n):
    global white,blue
    check=data[x][y]

    if n==0:
        return

    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=data[i][j]:
                n//=2
                division(x,y,n)
                division(x,y+n,n)
                division(x+n,y,n)
                division(x+n,y+n,n)

                return
    if check==0:
        white+=1
    if check==1:
        blue+=1
    return
division(0,0,n)
print(white)
print(blue)