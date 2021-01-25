"""
https://leetcode.com/problems/distinct-subsequences/

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It's guaranteed the answer fits on a 32-bit signed integer.

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
    
    
func numDistinct(s string, t string) int {
    m, n := len(s), len(t)
    dp := make([][]int, m + 1)
    for i := 0; i < m + 1; i++ {
        dp[i] = make([]int, n + 1)
    }
    for i := 0; i < m + 1; i++ {
        dp[i][0] = 1
    }
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if s[i] == t[j] {
                dp[i+1][j+1] = dp[i][j] + dp[i][j+1]
            } else {
                dp[i+1][j+1] = dp[i][j+1]
            }
        }
    }

    return dp[m][n]
}
这里 没有想明白为什么i, j要反过来呢?
与直觉正好相反
"""


class Solution0:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(n + 1):
            dp[0][i] = 1
        for i in range(m):
            for j in range(n):
                if t[i] == s[j]:
                    dp[i + 1][j + 1] = dp[i][j] + dp[i + 1][j]
                else:
                    dp[i + 1][j + 1] = dp[i + 1][j]
        return dp[m][n]


# 缺乏把问题抽象化的能力
# 数学建模的重要性

class Solution1:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}

        def f(s, t):
            if not t:
                return 1
            if not s:
                return 0
            key = (s, t)
            if key in memo:
                return memo[key]
            val = f(s[:-1], t) + (f(s[:-1], t[:-1]) if s[-1] == t[-1] else 0)
            memo[key] = val
            return val

        return f(s, t)


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        memo = {}

        def f(i, j):
            if j < 0:
                return 1
            if i < 0:
                return 0
            key = (i, j)
            if key in memo:
                return memo[key]
            # s[i] == t[j] means s[i] matches t[j]
            # using s[i] to match t[j]
            # using s[i-1] to match t[j]
            # using s[i-2] to match t[j]
            # ...
            val = f(i - 1, j) + (f(i - 1, j - 1) if s[i] == t[j] else 0)
            memo[key] = val
            return val

        return f(m - 1, n - 1)


# 转台转义方程为什么是这个?
# 你能解释清楚吗?

if __name__ == '__main__':
    S = "rabbbit"
    T = "rabbit"
    print(Solution().numDistinct(S, T))

    S = "babgbag"
    T = "bag"
    print(Solution().numDistinct(S, T))
