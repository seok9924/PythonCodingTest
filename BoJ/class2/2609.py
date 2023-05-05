def gcd(a,b):
    if a%b==0:
        return b


    return gcd(b,a%b)

a,b=map(int,input().split())

t=gcd(a,b)

print(t)
print((a//t)*b)