"""
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

"""
from typing import List


class Solution0:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res, cnt = 0, 0
        for i, e in enumerate(nums):
            if i > 0 and e == nums[i - 1] + 1:
                cnt += 1
            else:
                cnt = 1
            res = max(res, cnt)
        return res


class Solution1:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        dp = [0] * len(nums)
        for i, e in enumerate(nums):
            if i == 0:
                dp[i] = 1
            else:
                dp[i] = dp[i - 1] + (1 if e == nums[i - 1] + 1 else 0)
        print(nums)
        print(dp)
        return dp[-1]


# 前两个都是失败的思路, 不值得借鉴

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in nums:
            # searching for start point
            # not every point will be checked
            if n - 1 not in s:
                j = n + 1
                while j in s:
                    j += 1
                res = max(res, j - n)
        return res


# T: O(n * 2)
# n - 1, j + 1 正好把这个数组遍历了两遍

# 还是这个思路比较简单


if __name__ == '__main__':
    print(Solution().longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(Solution().longestConsecutive([1, 2, 0, 1]))
    print(Solution().longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
