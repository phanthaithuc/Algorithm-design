# Given a list of intervals calendar and a number of available conference rooms. For each query,
# return true if the meeting can be added to the calendar
# successfully without causing a conflict, otherwise false.
# A conference room can only hold one meeting at a time.
#
# Example 1:
#
# Input: calendar = [[1, 2], [4, 5], [8, 10]], rooms = 1, queries = [[2, 3], [3, 4]]
# Output: [true, true]
# Example 2:
#
# Input: calendar = [[1, 2], [4, 5], [8, 10]], rooms = 1, queries = [[4, 5], [5, 6]]
# Output: [false, true]
# Example 3:
#
# Input:
# calendar = [[1, 3], [4, 6], [6, 8], [9, 11], [6, 9], [1, 3], [4, 10]]
# rooms = 3
# queries = [[1, 9], [2, 6], [7, 9], [3, 5], [3, 9], [2, 4], [7, 10], [5, 9], [3, 10], [9, 10]]
# Output: [false, true, false, true, false, true, false, false, false, true]


import bisect
import unittest
from collections import defaultdict


class SegmentTree:
    def __init__(self, n):
        self.tree = [0] * (n * 4 + 10)
        self.n = n

    def update(self, pos, left, right, idx, val):
        if idx < left or idx > right:
            return
        if left == right:
            self.tree[pos] = val
            return
        mid = (left + right) // 2
        self.update(pos * 2 + 1, left, mid, idx, val)
        self.update(pos * 2 + 2, mid + 1, right, idx, val)
        self.tree[pos] = max(self.tree[pos * 2 + 1], self.tree[pos * 2 + 2])
        return

    def query(self, pos, left, right, ql, qr):
        if qr < left or ql > right:
            return 0
        if ql <= left and qr >= right:
            return self.tree[pos]
        mid = (left + right) // 2
        return max(self.query(pos * 2 + 1, left, mid, ql, qr), self.query(pos * 2 + 2, mid + 1, right, ql, qr))


class Solution(object):
    def isAvaiblable(self, calender, rooms, queries):
        cnt = defaultdict(int)
        for start, end in calender:
            cnt[start] += 1
            cnt[end] -= 1
        times = sorted(cnt)
        intervals = [0]
        for t in times:
            intervals.append(cnt[t] + intervals[-1])

        # print(times,intervals)
        n = len(intervals)
        T = SegmentTree(n)
        for i, v in enumerate(intervals):
            T.update(0, 0, n - 1, i, v)
        res = []
        for start, end in queries:
            ql = bisect.bisect_right(times, start)
            qr = bisect.bisect_left(times, end)
            # print(start, end, ql,qr)
            # res.append(max([intervals[i] for i in range(ql,qr+1)]) < rooms)
            res.append(T.query(0, 0, n - 1, ql, qr) < rooms)

        return res


class TestStringMethods(unittest.TestCase):

    def test_1(self):
        calender = [[1, 2], [4, 5], [8, 10]]
        rooms = 1
        queries = [[2, 3], [3, 4]]
        output = [True, True]
        test = Solution()
        self.assertEqual(test.isAvaiblable(calender, rooms, queries), output)

    def test_2(self):
        calender = [[1, 2], [4, 5], [8, 10]]
        rooms = 1
        queries = [[4, 5], [5, 6]]
        output = [False, True]
        test = Solution()
        self.assertEqual(test.isAvaiblable(calender, rooms, queries), output)

    def test_3(self):
        calender = [[1, 3], [4, 6], [6, 8], [9, 11], [6, 9], [1, 3], [4, 10]]
        rooms = 3
        queries = [[1, 9], [2, 6], [7, 9], [3, 5], [3, 9], [2, 4], [7, 10], [5, 9], [3, 10], [9, 10]]
        output = [False, True, False, True, False, True, False, False, False, True]
        test = Solution()
        self.assertEqual(test.isAvaiblable(calender, rooms, queries), output)


if __name__ == '__main__':
    unittest.main()
