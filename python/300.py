"""
https://leetcode.com/problems/longest-increasing-subsequence/


Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

"""

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


if __name__ == '__main__':
    nums = [10,9,2,5,3,7,101,18]
    print(nums)
    print(Solution().lengthOfLIS(nums))

    nums = [4,10,4,3,8,9]
    print(nums)
    print(Solution().lengthOfLIS(nums))

