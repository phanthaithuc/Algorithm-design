# Given an integer array nums and an integer k,
# return the k most frequent elements. You may return the answer in any order.
import heapq
from collections import Counter


def topK(nums: [], k: int) -> []:
    if k == len(nums):
        return nums

    count = Counter(nums)
    print(count.keys())
    return heapq.nlargest(k, count.keys(), key= count.get)


print(topK([1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 44, 4], 3))
