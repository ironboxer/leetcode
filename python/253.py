"""
https://leetcode.com/problems/meeting-rooms-ii/

253. 会议室 II
给定一个会议时间安排的数组，每个会议时间都会包括开始和结束的时间 [[s1,e1],[s2,e2],...] (si < ei)，为避免会议冲突，同时要考虑充分利用会议室资源，请你计算至少需要多少间会议室，才能满足这些会议安排。

示例 1:

输入: [[0, 30],[5, 10],[15, 20]]
输出: 2
示例 2:

输入: [[7,10],[2,4]]
输出: 1
"""

from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        A, B = sorted([e[0] for e in intervals]), sorted([e[1] for e in intervals])
        room, N = 0, len(A)
        start, end = 0, 0
        while start < N:

            if A[start] >= B[end]:
                end += 1
            else:
                room += 1

            start += 1

        return room


import heapq

# 整理后的思路是什么 为什么没有结论呢?

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervalSort = sorted(intervals, key=lambda item: item[0])
        h = []
        h.append(intervalSort[0][1])
        heapq.heapify(h)
        for i in range(1, len(intervalSort)):
            start, end = intervalSort[i]
            if start >= h[0]:
                heapq.heappushpop(h, end)
            else:
                heapq.heappush(h, end)
        return len(h)


from heapq import heappush, heappop, heappushpop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort by start time
        intervals.sort(key=lambda x: x[0])
        h = []
        for start, end in intervals:
            if not h:
                h.append(end)
            # start time >= most end time
            elif start >= h[0]:
                # update most end time
                heappushpop(h, end)
            else:
                # new start time < old end time -> need new rooms
                heappush(h, end)

        return len(h)


if __name__ == '__main__':
    intervals = [[0, 30],[5, 10],[15, 20]]
    print(Solution().minMeetingRooms(intervals))


    intervals = [(1, 10), (2, 7), (3, 19), (8, 12), (10, 20), (11, 30)]
    print(Solution().minMeetingRooms(intervals))

