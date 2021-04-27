nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
from typing import List


def longestConsecutiveSequence(nums) -> List[int]:
    if not nums:
        return 0
    nums.sort()
    curr_streak = 1
    streak = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if nums[i] == nums[i - 1] + 1:
                curr_streak += 1
                streak = max(streak, curr_streak)
            else:

                curr_streak = 1
    return streak


def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    longest_streak = 0
    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            while current_num 

print(longestConsecutiveSequence([0, 0]))
