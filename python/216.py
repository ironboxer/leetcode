"""
https://leetcode.com/problems/combination-sum-iii/

Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

Note:

All numbers will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: k = 3, n = 7
Output: [[1,2,4]]

Example 2:

Input: k = 3, n = 9
Output: [[1,2,6], [1,3,5], [2,3,4]]

"""

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def f(pos, buf):
            if len(buf) == k:
                if sum(buf) == n:
                    res.append(buf[:])
                return
            for i in range(pos, 10):
                buf.append(i)
                f(i+1, buf)
                buf.pop()
        f(1, [])

        return res

if __name__ == '__main__':
    print(Solution().combinationSum3(3, 7))
    print(Solution().combinationSum3(3, 9))

