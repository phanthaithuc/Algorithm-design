class Solution:
    def __init__(self, nums):
        self.nums = nums

    def twoSum(self, target) -> []:
        i = j = 0
        res = []
        while i< len(self.nums):
            while j < len(self.nums):
                if self.nums[i]+ self.nums[j] == target:
                    res.append(i)
                    res.append(j)
                j+=1
            i+=1
        return res

    def twoSum2(self, target) -> []:
        j = 0
        h = {}
        res = []
        while j < len(self.nums):
            k = target - self.nums[j]

            if k in h:
                res.append(h.get(k))
                res.append(j)
            h[self.nums[j]] = j

            j+=1
        return res

if __name__== "__main__"
    nums = [2,11,15,7]
    nums2 = [3,2,4,5]
    solution = Solution(nums2)
    print(solution.twoSum2(6))

