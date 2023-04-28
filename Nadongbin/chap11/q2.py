s= input()
# s='567'
length=len(s)

total =0

for i in range(length):
    value= int(s[i])
    
    if total<=1 :
        total+=value
    else:
        if value <=1 :
            total+=value
        else:
            total*=value
            
print(total)