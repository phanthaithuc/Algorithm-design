from typing import List

def missing_range(nums: List[int], low: int, high: int):
    s = set(range(low, high + 1))
    res = []
    for i in range(len(nums) - 1):
        nums_set = set(range(nums[i], nums[i+1]))
        intersection = s.intersection(nums_set)
        res.append(intersection)
    return res


print(missing_range([1,3,5,10], 1, 10))


