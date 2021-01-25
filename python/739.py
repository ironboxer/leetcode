"""
https://leetcode.com/problems/daily-temperatures

739. Daily Temperatures
Medium

3382

102

Add to List

Share
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""


from typing import List


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        total = len(T)
        res = [0] * total
        stack = []
        for i in range(total - 1, -1, -1):
            n = T[i]
            while stack and T[stack[-1]] <= n:
                stack.pop()
            res[i] = stack[-1] - i if stack else 0
            stack.append(i)
        return res


if __name__ == '__main__':
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(Solution().dailyTemperatures(T))


