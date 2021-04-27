import heapq

from typing import List


def meetingRoom(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0

    def get_x(x):
        print(x[0])
        return x[0]
    get_x(intervals)
    intervals.sort(key=lambda x: x[0])
    room = [intervals[0][1]]

    for meeting in intervals[1:]:

        if room[0] <= meeting[0]:
            heapq.heappop(room)
        heapq.heappush(room, meeting[1])

    return len(room)


print(meetingRoom([[0, 30], [5, 10], [15, 20], [50, 25], [5, 15]]))
