"""
https://leetcode.com/problems/decode-ways/

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        for i, e in enumerate(s):
            if e != '0':
                dp[i + 1] = dp[i]
            if i > 0 and 10 <= int(s[i - 1:i + 1]) <= 26:
                # 实际上是想要表达 dp[i] = dp[i-2]
                dp[i + 1] += dp[i - 1]
        # print(dp)
        return dp[n]


class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            if 1 <= int(s[i]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i-1:i+1]) <= 26:
                # 这是一个补丁
                # i - 2 < 0
                if i > 2:
                    dp[i] += dp[i-2]
                else:
                    dp[i] += 1

        # print(dp)
        return dp[-1]


# 你真的明白了吗? 需要列出几个case, 然后总结状态转移方程

if __name__ == '__main__':
    s = '12'
    print(Solution().numDecodings(s))

    s = '226'
    print(Solution().numDecodings(s))

    s = '012'
    print(Solution().numDecodings(s))

    s = '12120'
    print(Solution().numDecodings(s))
