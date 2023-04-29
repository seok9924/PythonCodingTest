n= input()

length=len(n)
left=n[0:length//2]
right=n[length//2:length]

lsum=0
rsum=0
for i in range(length//2):
    lsum+=int(left[i])
    rsum+=int(right[i])

if lsum==rsum:
    print("Lucky")
else:
    print("Ready")