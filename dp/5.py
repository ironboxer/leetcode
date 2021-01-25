"""
https://leetcode.com/problems/longest-palindromic-substring/
需要注意很多边界条件
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res, N = "", len(s)
        dp = [[False] * N for _ in range(N)]
        # dp[i][j] = dp[i+1][j-1] if s[i] == s[j]
        for i in range(N-1, -1, -1):
            for j in range(i, N):
                # print(i, j, s[i:j+1])
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j and s[i] == s[j]:
                    dp[i][j] = True
                else:
                    if s[i] == s[j]:
                        dp[i][j] |= dp[i+1][j-1]
                if dp[i][j]:
                    if j - i + 1 > len(res):
                        res = s[i: j+1]
        return res


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
    print(Solution().longestPalindrome("cbbd"))
