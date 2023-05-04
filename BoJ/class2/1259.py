import sys
from os import path
if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")

a='x'
while a!=0:
    answer=''
    a=int(input())
    if a==0:
        break
    penlin=str(a)
    length=len(penlin)
    if length%2==0:
        for i in range(length//2):
            if penlin[i]!=penlin[length-1-i]:
                answer="no"
                break

    else:
        for i in range(length//2):
            if penlin[i]!=penlin[length-1-i]:
                answer="no"
                break


    if answer=="no":
        print(answer)
    else:
        print("yes")




