# import sys
# from os import path
# if path.exists('input.txt'):
#     sys.stdin = open("input.txt", "r")

n=int(input())

a=[]
for i in range(n):
    a.append(int(input()))


zeros=[1,0,1]
ones=[0,1,1]


for i in range(3,max(a)+1):
    zeros.append(zeros[i-2]+zeros[i-1])
    ones.append(ones[i-2]+ones[i-1])

for i in a:
    print(zeros[i],ones[i])