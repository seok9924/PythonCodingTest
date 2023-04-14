
input =[0,3,7,2,5,8,4,6,0,1]





def longestConsecutive(nums):
    longest=0
    num_dict={}
    for num in nums:
        num_dict[num]=True

    for num in num_dict:
        cnt=0
        if num-1 not in num_dict:
            cnt+=1
            target=num+1
            while target in num_dict:
                target+=1
                cnt+=1
            longest=max(longest,cnt)
    return longest

print(longestConsecutive(input))