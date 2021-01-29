class Counter():
    def __init__(self, nums):
        self.nums = nums

    def count(self):
        d = {}
        for i in self.nums:
            d[i] = nums.count(i)

        for key, value in d.items():
            if value == 1:
                print(key)

    def minus(self):
        for i in range(len(nums)):
            self.nums[self.nums[i]] *=-1
        print(self.nums)

if __name__=='__main__':
    nums = [4, 3, 2, 4, 1,3,2]
    counter = Counter(nums)
    counter.minus()

