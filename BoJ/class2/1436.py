n= int(input())

a=666
for i in range(n-1):
    x = a

    while True:

        if '666' in str(x) and x>a:
            a=x
            break
        x+=1
print(a)
