"""
https://leetcode.com/problems/minimum-size-subarray-sum/

Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 

Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 

"""

from typing import List


# naive 的版本
class Solution0:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        n = len(nums)
        t = n
        for i in range(n):
            r = 0
            for j in range(i, n):
                r += nums[j]
                if r >= s:
                    t = min(t, j - i + 1)
        return t


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        l, r, cur, res, n = 0, 0, 0, 999999, len(nums)
        while r < n:
            cur += nums[r]
            while cur >= s and l <= r:
                res = min(res, r - l + 1)
                cur -= nums[l]
                l += 1

            r += 1

        return res if res < 999999 else 0


# a very simple solution

class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        last = 0
        cur = 0
        cnt = 999999
        for i, e in enumerate(nums):
            cur += e
            while cur >= s:
                cnt = min(cnt, i - last + 1)
                cur -= nums[last]
                last += 1
        return cnt if cnt < 999999 else 0


if __name__ == '__main__':
    s = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(s, nums))

    s = 3
    nums = [1, 1]
    print(Solution().minSubArrayLen(s, nums))
