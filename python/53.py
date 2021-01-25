"""
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [0]
Output: 0
Example 4:

Input: nums = [-1]
Output: -1
Example 5:

Input: nums = [-2147483647]
Output: -2147483647
 

Constraints:

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1

"""

from typing import List


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = nums[:]
        for i in range(len(nums)):
            if i > 0 and dp[i - 1] > 0:
                dp[i] += dp[i - 1]
        return max(dp)


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


class Solution:
    """
    为什么这种方式会更慢呢?
    完全搞不懂啊
    """
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -2 ** 31
        for i in range(len(nums)):
            if i > 0 and nums[i - 1] > 0:
                nums[i] += nums[i - 1]
            max_sum = max(max_sum, nums[i])
        return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
