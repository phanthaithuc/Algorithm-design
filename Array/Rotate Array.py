nums = [12, 16, 17, 2, 4, 11]

j = len(nums) - 1
m = min(nums)

while j >= 0:
    nums[j], m = m, max(nums[j], m)
    j -= 1

print(nums)
