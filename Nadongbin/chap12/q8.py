ddict={}
for i in range(65,91):
    ddict[chr(i)]=0

for i in range(0,10):
    ddict[str(i)]=0

s= input()

for i in s:
    ddict[i]+=1


for e,v in ddict.items():
    if v==0:
        continue
    else:
        for i in range(v):
            print(e, end="")

