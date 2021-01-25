"""
https://leetcode.com/problems/partition-equal-subset-sum/

Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""


from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if bool(s & 1):
            return False

        s //= 2
        n = len(nums)
        # 在集合中找到一半的元素 使得和为s
        dp = [[False] * (s + 1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1, n + 1):
            for j in range(1, s + 1):
                if j < nums[i-1]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]

        return dp[n][s]

























class Solution:
     def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        # odd case
        if s // 2 * 2 != s:
            return False

        nums.sort()
        memo = {}
        def f(s, i):
            val = memo.get(s)
            if val is not None:
                return val
            if s == 0:
                val = True
                memo[s] = val
                return val
            if i == len(nums):
                val = False
                memo[s] = val
                return val
            for j in range(i, len(nums)):
                n = nums[i]
                if n > s:
                    break
                if f(s - n, j + 1) or f(s, j + 1):
                    val = True
                    memo[s] = val
                    return val
            val = False
            memo[s] = val
            return val

        return f(s // 2, 0)


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if (s >> 1) << 1 != s:
            return False
        s >>= 1
        n = len(nums)
        dp = [[False] * (s + 1) for _ in range(n + 1)]
        # 这里的初始化非常关键 表示 sum==0时为true
        for i in range(n+1):
            dp[i][0] = True
        for i in range(n):
            # j表示重量 应该从1开始才是有意义的
            for j in range(1,s + 1):
                if nums[i] <= j:
                    dp[i+1][j] = dp[i][j-nums[i]] or dp[i][j]
                else:
                    dp[i+1][j] = dp[i][j]
        for row in dp:
            print(row)
        return dp[n][s]



if __name__ == '__main__':
    nums = [1,5,11,5]
    print(Solution().canPartition(nums))

    nums = [1,2,3,5]
    print(Solution().canPartition(nums))

