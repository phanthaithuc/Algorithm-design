class rangesumarray:
    def __init__(self, nums: []):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        while i <= j:
            sum += self.nums[i]
            i += 1

        return sum

    def caching(self) -> int:
        sum = {}
        for i in range(len(self.nums)):
            for j in range(len(self.nums)):
                sum[i, j] = self.nums[i] + self.nums[j]
        # print(sum)
        return sum




nums = [-2, 0, 3, -5, 2, -1]
NumArray = rangesumarray(nums)
print(NumArray.sumRange(0, 2))
print(NumArray.sumRange(2, 5))
print(NumArray.sumRange(0, 5))
h = NumArray.caching()

print(h.keys())
i = 0
j = 2

if i in h and j in h:
    print(h.value)
    print("sucess")
