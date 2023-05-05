import math

m,n =map(int,input().split())
a=[]
for i in range(m,n+1):
    check=True
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            check=False
            break
    if check and i!=1:
        print(i)
