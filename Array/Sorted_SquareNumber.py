nums = [-7, -6, -5, 0, 1, 2, 3, 4, 5]
res = [0] * len(nums)
head = 0
index = tail = len(nums)-1

while head < tail:
    if abs(nums[head]) >= abs(nums[tail]):
        res[index] = nums[head] ** 2
        index -= 1
        head += 1
    else:
        res[index] = nums[tail] ** 2
        tail -= 1
        index -= 1

print(res)

print(nums)
print(len(nums) == len(res))

