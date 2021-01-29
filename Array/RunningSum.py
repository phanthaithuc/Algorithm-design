nums = [3,1,2,10,1]
res = []
sum = 0
for i, v in enumerate(nums):
    sum += v
    res.append(sum)

print(res)