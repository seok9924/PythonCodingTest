s= input()
# s='00011001100'

onecount=0 
zerocount= 0

if s[0]=='1':
    onecount+=1
else:
    zerocount+=1

for i in range(1,len(s)):
    
    
    if s[i]=='1':
        if s[i-1]==s[i]:
            continue
        else:
            zerocount+=1
        
    else: 
        if s[i-1]== s[i] :
            continue
        else:
            onecount+=1
            
print(min(onecount,zerocount))