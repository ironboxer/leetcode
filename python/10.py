"""
https://leetcode.com/problems/regular-expression-matching/

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false

最先想到的是递归的方法, 但是buttom up的方法也要会
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        def f(i, j):
            if j == n:
                return i == m
            cond = i < m and (s[i] == p[j] or p[j] == '.')
            if j + 1 < n and p[j+1] == '*':
                if cond:
                    return f(i+1, j) or f(i, j+2)
                return f(i, j+2)
            if cond:
                return f(i+1, j+1)
            return False
        return f(0, 0)


# 记录匹配情况
class Solution2:
    def isMatch(self, s: str, p: str) -> bool:
        from functools import lru_cache
        m, n = len(s), len(p)

        @lru_cache
        def f(i, j):
            ret = memo.get((i, j))
            if ret is not None:
                return ret
            if j == n:
                return i == m
            cond = i < m and (s[i] == p[j] or p[j] == '.')
            if j + 1 < n and p[j+1] == '*':
                if cond:
                    return f(i+1, j) or f(i, j+2)
                return f(i, j+2)
            if cond:
                return f(i+1, j+1)
            return False
        return f(0, 0)


# buttom up version
# bufttom up version 最接近dp的本质, 但是和人类的思维方式相反, 不如递归更加符合人类的思维

class Solution3:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for i in range(m+1)]
        dp[-1][-1] = True
        for i in range(m, -1, -1):
            for j in range(n-1, -1, -1):
                cond = i < m and (s[i] == p[j] or p[j] == '.')
                if j + 1 < n and p[j+1] == '*':
                    if cond:
                        dp[i][j] = dp[i+1][j] or dp[i][j+2]
                    else:
                        dp[i][j] = dp[i][j+2]
                elif cond:
                    dp[i][j] = dp[i+1][j+1]
        return dp[0][0]

# 其中, i  为甚磨从m开始, 就是要考虑到s为空串, 需要满足 dp[i][j] = dp[i][j+2]的情况
# 所以 i 从m开始





















class Solution:
    """
    这个递归的算法虽然很长
    但是思路是很清晰的
    你一定忘不了
    """
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def f(s, p):
            key = (s, p)
            val = memo.get(key)
            if val is not None:
                return val

            if not p:
                val = not s
                memo[key] = val
                return val
            if not s:
                val = len(p) > 1 and p[1] == '*' and f(s, p[2:])
                memo[key] = val
                return val
            if len(p) > 1 and p[1] == '*':
                if s[0] == p[0] or p[0] == '.':
                    val = f(s[1:], p[2:]) or f(s[1:], p) or f(s, p[2:])
                    memo[key] = val
                    return val
                val = f(s, p[2:])
                memo[key] = val
                return val
            if s[0] == p[0] or p[0] == '.':
                val = f(s[1:], p[1:])
                memo[key] = val
                return val
            val = False
            memo[key] = val
            return val

        return f(s, p)


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 表示 s p 都是 空串的时候 应为True
        dp[m][n] = True
        for i in range(m, -1, -1):
            for j in range(n-1, -1, -1):
                if j + 1 < n and p[j+1] == '*':
                    if i < m and (s[i] == p[j] or p[j] == '.'):
                        dp[i][j] = dp[i][j+2] or dp[i+1][j+2] or dp[i+1][j]
                    else:
                        dp[i][j] = dp[i][j+2]
                elif i < m and (s[i] == p[j] or p[j] == '.'):
                    dp[i][j] = dp[i+1][j+1]

        return dp[0][0]


if __name__ == "__main__":
    cases = [
        ("", "", True),
        ("", ".*", True),
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
    ]
    for s, p, r in cases:
        print(s, p, r)
        assert Solution().isMatch(s, p) == r

