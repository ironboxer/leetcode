"""
https://leetcode.com/problems/combination-sum-iv/

Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.

Example:

nums = [1, 2, 3]
target = 4

The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)

Note that different sequences are counted as different combinations.

Therefore the output is 7.


Follow up:
What if negative numbers are allowed in the given array?
How does it change the problem?
What limitation we need to add to the question to allow negative numbers?

Credits:
Special thanks to @pbrother for adding this problem and creating all test cases.

"""

from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = []
        def f(s, buf):
            if s == 0:
                res.append(buf[:])
                return
            for i, e in enumerate(nums):
                if e > s:
                    break
                buf.append(e)
                f(s - e, buf)
                buf.pop()

        f(target, [])

        print(res)
        return len(res)


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        res = 0
        def f(s):
            if s == 0:
                nonlocal res
                res += 1
                return
            for i, e in enumerate(nums):
                if e > s:
                    break
                f(s - e)
        f(target)

        return res


class SolutionX:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()

        def f(s):
            if s == 0:
                return 1
            r = 0
            for e in nums:
                if e > s:
                    break
                r = max(r, f(s - e))
            return r

        return f(target)


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for e in nums:
                if i >= e:
                    dp[i] += dp[i - e]
        print(dp)
        return dp[target]


class Solution:
    """
    这是最简单的方式, 可以结合递归的方式比较理解
    """
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp = [1] + [0] * target
        for i in range(1, target + 1):
            for n in nums:
                if n > i:
                    break
                dp[i] += dp[i-n]

        return dp[target]


if __name__ == '__main__':
    nums = [1, 2, 3]
    target = 4
    print(Solution().combinationSum4(nums, target))

    nums = [4, 2, 1]
    target = 32
    print(Solution().combinationSum4(nums, target))

