import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")



t= int(input())

d={1:1,2:1,3:1,4:2,5:2,6:3}
def dp(x):

    if x==0:
        return
    if x==1 or x==2 or x==3:
        return 1
    if x==4 or x==5:
        return 2

    else:
        if x in d:
            return d[x]
        else:
            d[x]=dp(x-1)+dp(x-5)
    return d[x]

for i in range(t):
    x= int(input())
    print(dp(x))


