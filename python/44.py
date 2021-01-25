"""
https://leetcode.com/problems/wildcard-matching/

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""


class Solution1:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import lru_cache

        @lru_cache
        def f(s, p):
            if not p:
                return not s
            if not s:
                return p[0] == '*' and f(s, p[1:])
            if s[0] == p[0] or p[0] == '?':
                return f(s[1:], p[1:])
            if p[0] == '*':
                return f(s[1:], p[1:]) or f(s, p[1:]) or f(s[1:], p)
            return False

        return f(s, p)


class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def f(i, j):
            key = (i, j)
            if key in memo:
                return memo[key]
            if j == n:
                r = i == m
                memo[key] = r
                return r
            if i == m:
                r = p[j] == '*' and f(i, j + 1)
                memo[key] = r
                return r
            if s[i] == p[j] or p[j] == '?':
                r = f(i + 1, j + 1)
                memo[key] = r
                return r
            if p[j] == '*':
                r = f(i + 1, j + 1) or f(i + 1, j) or f(i, j + 1)
                memo[key] = r
                return r
            return False

        return f(0, 0)


# 为什么这个递归的方式不行呢?
# 为什么加上缓存之后又可以了?
# 说明还是没有彻底搞懂啊?

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[-1][-1] = True
        for i in range(m, -1, -1):
            for j in range(n - 1, -1, -1):
                if p[j] == '*':
                    dp[i][j] = i < m and (dp[i + 1][j + 1] or dp[i + 1][j]) or dp[i][j + 1]
                elif i < m and (s[i] == p[j] or p[j] == '?'):
                    dp[i][j] = dp[i + 1][j + 1]

        return dp[0][0]




























from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @lru_cache
        def f(s, p):
            if not p:
                return not s
            if not s:
                return f(s, p[1:]) if p[0] == '*' else False
            if p[0] == '*':
                return f(s[1:], p) or f(s[1:], p[1:]) or f(s, p[1:])
            if s[0] == p[0] or p[0] == '?':
                return f(s[1:], p[1:])

            return False

        return f(s, p)



# 不用字符串 改为指针 速度会快一点
from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        @lru_cache
        def f(i, j):
            if j == n:
                return i == m
            if i == m:
                return f(i, j+1) if p[j] == '*' else False
            if p[j] == '*':
                return f(i+1, j) or f(i+1, j+1) or f(i, j+1)
            if s[i] == p[j] or p[j] == '?':
                return f(i+1, j+1)

            return False

        return f(0, 0)


# 动态规划的版本



class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True
        for i in range(m, -1, -1):
            for j in range(n-1, -1, -1):
                if p[j] == '*':
                    if i < m:
                        dp[i][j] = dp[i+1][j] or dp[i+1][j+1] or dp[i][j+1]
                    else:
                        dp[i][j] = dp[i][j+1]
                elif i < m and (s[i] == p[j] or p[j] == '?'):
                    dp[i][j] = dp[i+1][j+1]

        return dp[0][0]



# 比之前的那道题更加简单

if __name__ == "__main__":
    cases = [
        ("aa", "a", False),
        ("aa", "*", True),
        ("cb", "?a", False),
        ("adceb", "*a*b", True),
        ("acdcb", "a*c?b?", False),
        ("", "******", True),
    ]
    for s, p, r in cases:
        print(s, p, r)
        t = Solution().isMatch(s, p)
        assert (t == r)

    s = "aaaaaabbaabaaaaabababbabbaababbaabaababaaaaabaaaabaaaabababbbabbbbaabbababbbbababbaaababbbabbbaaaaaaabbaabbbbababbabbaaabababaaaabaaabaaabbbbbabaaabbbaabbbbbbbaabaaababaaaababbbbbaabaaabbabaabbaabbaaaaba"
    p = "*bbb**a*******abb*b**a**bbbbaab*b*aaba*a*b**a*abb*aa****b*bb**abbbb*b**bbbabaa*b**ba**a**ba**b*a*a**aaa"
    print(Solution().isMatch(s, p))
