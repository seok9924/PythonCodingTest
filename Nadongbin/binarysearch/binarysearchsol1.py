
def binary_search(array,target,s,e):
    while s<=e:
        mid= (s+e)//2
        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            s=mid+1
        return None

n= int(input())

arr= list(map(int,input().split()))
arr.sort()

m=int(input())
targets=list(map(int,input().split()))

for target in targets:
    result=binary_search(arr,target,0,n-1)
    if result!=None :

        print("yes",end=' ')

    else:
        print("no",end=' ')
        
        
        

"""
계수정렬 사용하거나

혹은 

for target in targets:
    if target in arr:
    이런식으로 arr자체를 arr=set(map(int,input().split()))으로 받아버림


"""        
