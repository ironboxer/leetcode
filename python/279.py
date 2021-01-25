"""
https://leetcode.com/problems/perfect-squares/


Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""


class Solution:
    """
    searching: dfs or bfs
    """

    def numSquares(self, n: int) -> int:
        nums = []
        for i in range(1, n+1):
            v = i ** 2
            if v > n:
                break
            nums.append(v)
        memo = {}
        def f(n):
            if n == 0:
                return 0
            if n in memo:
                return memo[n]
            r = 999999
            for i in nums:
                if n < i:
                    break
                t = f(n-i) + 1
                r = min(r, t)
            memo[n] = r
            return r

        return f(n)


class Solution:
    def numSquares(self, n: int) -> int:
        nums = []
        for i in range(1, n+1):
            v = i ** 2
            if v > n:
                break
            nums.append(v)
        s = set(nums)
        dp = [999999] * (n + 1)
        dp[0] = 0
        dp[1] = 1
        for i in range(1, n+1):
            if i in s:
                dp[i] = 1
            else:
                dp[i] = min(dp[i-j] for j in nums) + 1

        return dp[n]


if __name__ == '__main__':
    for i in range(1, 50):
        print(i, Solution().numSquares(i))

