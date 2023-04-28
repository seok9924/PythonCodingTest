n=int(input())

a= list(map(int,input().split()))

a.sort()

target=1
for x in a:
    if target<x:
        break
    target+=x
print(target)