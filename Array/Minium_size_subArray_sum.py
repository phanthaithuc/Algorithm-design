import math
class Solution():
    def subArray(self, nums: [], s: int):
        sum_ = 0
        start = 0
        length = math.inf
        for i in range(len(nums)):
            sum_+= nums[i]
            while sum_ >= s:
                sum_ = sum_ - nums[start]
                length = min(length, i-start+1)
                start+=1

        return length if length < math.inf else 0



if __name__ == "__main__":
    nums = []
    s = 100
    res = Solution()
    print(res.subArray(nums,s))
