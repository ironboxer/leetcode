"""
https://leetcode.com/problems/merge-intervals/

Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.



Constraints:

intervals[i][0] <= intervals[i][1]
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        for i, j in intervals:
            if res and i <= res[-1][1]:
                res[-1][1] = max(res[-1][1], j)
            else:
                res.append([i, j])
        return res

















class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        res = []
        for i, interval in enumerate(intervals):
            if i == 0:
                res.append(interval)
            else:
                # 这里还需要稍微判断一下
                if interval[0] <= res[-1][1]:
                    res[-1][1] = max(res[-1][1], interval[1])
                else:
                    res.append(interval)

        return res


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(Solution().merge(intervals))

    intervals = [[1, 4], [4, 5]]
    print(Solution().merge(intervals))

    intervals = [[1, 4], [2, 3]]
    print(Solution().merge(intervals))

    intervals = [[1, 4], [1, 5]]
    print(Solution().merge(intervals))

