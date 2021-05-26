# Given an array of intervals intervals
# where intervals[i] = [starti, endi],
# return the minimum number of intervals
# you need to remove to make the rest of the intervals non-overlapping.

from typing import List

intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
intervals2 = [[1, 2], [1, 2], [1, 2]]
intervals3 = [[1, 2], [2, 3]]
intervals4 = [[1, 100], [11, 22], [1, 11], [2, 12]]


def eraseOverlapIntervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[0])
    non_interval_list = []

    for interval in intervals:
        if not non_interval_list or non_interval_list[-1][1] <= interval[0]:
            non_interval_list.append(interval)

    return len(intervals) - len(non_interval_list)


def interval_calc(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])
    merge = []
    for interval in intervals:
        if not merge or merge[-1][1] <= interval[0]:
            merge.append(interval)
        #else:
            #cnt += 1
    return merge


def greedy(intervals: List[List[int]]) -> int:
    end = float("-inf")
    cnt = 0
    for start, e in sorted(intervals, key=lambda x: x[1]):
        if start >= end:
            end = e
        else:
            cnt += 1

    return cnt


print(eraseOverlapIntervals(intervals4))
print(interval_calc(intervals4))
print(" greedy: ", greedy(intervals4))
