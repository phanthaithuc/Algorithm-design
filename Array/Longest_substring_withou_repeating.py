import collections

res = []
nums = [-1,0,1,2,-1,-4,-3,1,0,4,0,1,1]
i = 0
k = 3
current_sum = 0
while i < len(nums):
    current_sum+= nums[i]
    if i >= k-1:
        if current_sum == 0:
            res.append([nums[i-(k-1)], nums[i-1], nums[i]])
        current_sum-= nums[i-(k-1)]
    i+=1

print(res)
