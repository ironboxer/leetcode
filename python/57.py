"""
https://leetcode.com/problems/insert-interval/

Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

public List<Interval> insert(List<Interval> intervals, Interval newInterval) {
    List<Interval> result = new LinkedList<>();
    int i = 0;
    // add all the intervals ending before newInterval starts
    while (i < intervals.size() && intervals.get(i).end < newInterval.start)
        result.add(intervals.get(i++));
    // merge all overlapping intervals to one considering newInterval
    while (i < intervals.size() && intervals.get(i).start <= newInterval.end) {
        newInterval = new Interval( // we could mutate newInterval here also
                Math.min(newInterval.start, intervals.get(i).start),
                Math.max(newInterval.end, intervals.get(i).end));
        i++;
    }
    result.add(newInterval); // add the union of intervals we got
    // add all the rest
    while (i < intervals.size()) result.add(intervals.get(i++));
    return result;
}

"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []
        for i, j in intervals:
            if res and res[-1][1] >= i:
                res[-1][1] = max(res[-1][1], j)
            else:
                res.append([i, j])
        return res



class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        if not intervals:
            res.append(newInterval)
            return res

        if newInterval[1] < intervals[0][0]:
            res.append(newInterval)
            res.extend(intervals)
            return res

        if newInterval[0] >  intervals[-1][1]:
            res.extend(intervals)
            res.append(newInterval)
            return res

        l, r, flag = 1 << 31, -(1 << 31), False

        for i, (a, b) in enumerate(intervals):
            if i + 1 < len(intervals) and b < newInterval[0] and newInterval[1] < intervals[i+1][0]:
                res.append([a, b])
                res.append(newInterval)
            elif b < newInterval[0] or a > newInterval[1]:
                if flag:
                    res.append([l, r])
                    flag = False
                res.append([a, b])
            else:
                l, r = min(l, a, newInterval[0]), max(r, b, newInterval[1])
                flag = True
        if flag:
            res.append([l, r])

        return res


# 很简单的一道题啊 就是做不对啊
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        res = []
        for a, b in intervals:
            if not res:
                res.append([a, b])
            else:
                if a > res[-1][1]:
                    res.append([a, b])
                else:
                    res[-1][1] = max(res[-1][1], b)

        return res


if __name__ == '__main__':
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    print(Solution().insert(intervals, newInterval))

    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    print(Solution().insert(intervals, newInterval))
