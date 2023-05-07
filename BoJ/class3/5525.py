import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n= int(input())
m=int(input())
s=input()
k=''
for i in range(2*n+1):
   if i%2==0:
       k+='I'
   else:
       k+="O"

count=0
steps=2*n+1
for i in range(m):
    if k in s[i:i+steps]:
        count+=1
print(count)
