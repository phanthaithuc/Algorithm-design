class Solution:
    def __init__(self, nums):
        self.nums = nums

    def arrayPairSum(self):
        arr = self.nums
        arr = sorted(arr)
        count = sum(arr[::2])
        return count

if __name__ == "__main__":
    nums = [1,4,3,2]
    res = Solution(nums).arrayPairSum()
    print(res)