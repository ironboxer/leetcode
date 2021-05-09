"""
https://leetcode.com/problems/longest-valid-parentheses/
"""


class Solution:
    def longestValidParentheses(self, s: str) -> int:
        N = len(s)
        if N == 0:
            return 0
        dp = [0] * N
        for i in range(1, N):
            if s[i] == ')':
                if s[i-1] == '(':
                    # at first, dp[i-2] is dp[-1], which is invalid, but dp[-1] is 0, so the result is ok
                    if i - 2 >= 0:
                        dp[i] = dp[i-2] + 2
                    else:
                        dp[i] = 2
                # s[i-1] == ')', check if s[i - dp[i-1]] == '('. if so,
                else:
                    if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                        dp[i] = dp[i - dp[i-1] - 2] + dp[i-1] + 2
        print(dp)
        return max(dp)


class Solution:
    """
    按照基本思路推理出来的版本
    """
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 2)
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif dp[i-1] and i - dp[i-1] - 1 >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i - dp[i-1] - 2] + dp[i-1] + 2

        return max(dp)


# 基本的思路就是这样, 这道题根本算不上动态规划, 其实就是简单的观察然后总结
# 但是你就是做不出来啊
# 问题在于你只是在抄袭答案 问题本省并不清楚

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        total = len(s)
        if total < 2:
            return 0
        # dp 表示已i结尾的字符串的最大长度
        # 连这个问题都定义不清楚 怎么做？
        dp = [0] * total
        for i in range(1, total):
            if s[i] == ')':
                # ()()
                if s[i-1] == '(':
                    dp[i] = 2 + (dp[i-2] if i > 2 else 0)
                else:
                    # ()(())
                    if dp[i-1] > 0 and i - 1 - dp[i-1] >= 0 and s[i - 1 - dp[i-1]] == '(':
                        dp[i] = 2 + dp[i-1] + (dp[i - 2 - dp[i-1]] if i - 2 - dp[i-1] > 0 else 0)

        return max(dp)


if __name__ == "__main__":
    cases = [
       (")()())", 4),
       (")())))", 2),
       ("()(())", 6),
       ("(()))())(", 4),
    ]
    for s, c in cases:
        r = Solution().longestValidParentheses(s)
        print(s, c, r)
        assert c == r

