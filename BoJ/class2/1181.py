import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n= int(input())
word=[]
for i in range(n):
    word.append(input())


a= list(set(word))
b=[]
for i in a:
    b.append((len(i),i))

print(sorted(b,key=lambda x:(x[0],x[1])))