# Given an array of intervals where
# intervals[i] = [starti, endi],
# merge all overlapping intervals,
# and return an array of the
# non-overlapping intervals that cover all the intervals in the input

from typing import List


def merge_intervals(intervals: List[List[int]]) -> List:
    intervals.sort(key=lambda x: x[0])
    merged = []
    for interval in intervals:
        f = interval[0]
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)

        else:
            merged[-1][1] = max(merged[-1][1], interval[1])
    return merged


print(merge_intervals(intervals=[[1, 3], [2, 6], [8, 10], [15, 18]]))
