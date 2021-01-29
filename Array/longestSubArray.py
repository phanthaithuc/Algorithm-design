#Find smallest sum >=8  of an array

class Solution:
    def bestsum(self, nums)-> int:
        curr_sum = 0
        best_sum =0
        for x in nums:
            curr_sum = max(0, curr_sum + x)
            best_sum = max(curr_sum, best_sum)
        return best_sum

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print(Solution().bestsum(nums))
    print(nums)
    print(nums.sort())
