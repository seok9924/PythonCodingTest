import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n= int(input())
word=[input() for _ in range(n)]


a= list(set(word))
b=[]
for i in a:
    b.append((len(i),i))

b=sorted(b,key=lambda x:(x[0],x[1]))

for i in b:
    print(i[1])
