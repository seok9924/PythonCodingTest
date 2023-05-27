import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

count=0
def recursion(s,l,r):
    global count
    global lastindex
    count+=1
    if (l>=r):
        return 1
    elif (s[l]!=s[r]):
        return 0
    else:
        return recursion(s,l+1,r-1)

def is_pelindrome(s):
    return recursion(s,0,len(s)-1)
t=int(input())
for i in range(t):
    x=input()
    a=is_pelindrome(x)
    print(a,count)
    count=0