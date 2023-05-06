import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

n,m= map(int,input().split())
dut={}
bo={}
dutbo=[]
count=0
for _ in range(n):
    dut[input()]=1

for _ in range(m):
    bo[input()]=1

for k,v in dut.items():
    if k in bo:
        dutbo.append(k)
        count+=1

print(count)
dutbo.sort()
for i in dutbo:
    print(i)