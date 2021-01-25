"""
https://leetcode.com/problems/regular-expression-matching/
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[-1][-1] = True
        for i in range(m, -1, -1):
            for j in range(n-1, -1, -1):
                # 优先处理
                if j + 1 < n and p[j+1] == '*':
                    if i < m and (s[i] == p[j] or p[j] == '.'):
                        dp[i][j] = dp[i+1][j] or dp[i][j+2]
                    else:
                        dp[i][j] = dp[i][j+2]
                # 一般情形
                elif i < m and (s[i] == p[j] or p[j] == '.'):
                    dp[i][j] = dp[i+1][j+1]
        # print(dp)
        return dp[0][0]


if __name__ == "__main__":
    cases = [
        ("aa", "a", False),
        ("aa", "a*", True),
        ("ab", ".*", True),
        ("aab", "c*a*b", True),
        ("mississippi", "mis*is*p*.", False),
    ]
    for s, p, r in cases:
        print(s, p, r)
        assert Solution().isMatch(s, p) == r
