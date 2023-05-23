import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

from itertools import  combinations
alpha=['a','e','i','o','u']
n,m= map(int,input().split())
strlist=input().split()
strlist.sort()
def check_string(s):
    aseries,bseries=0,0
    for i in range(len(s)):
        if s[i] in alpha:
            aseries+=1
        else:
            bseries+=1
    if aseries>=1 and bseries>=2:
        return True

    else:
        return False



for i in combinations(strlist,n):
    if check_string(i):
        print(''.join(list(i)))
    else:
        continue