"""
https://leetcode-cn.com/problems/longest-palindromic-subsequence/

516. 最长回文子序列
给定一个字符串 s ，找到其中最长的回文子序列，并返回该序列的长度。可以假设 s 的最大长度为 1000 。



示例 1:
输入:

"bbbab"
输出:

4
一个可能的最长回文子序列为 "bbbb"。

示例 2:
输入:

"cbbd"
输出:

2
一个可能的最长回文子序列为 "bb"。



提示：

1 <= s.length <= 1000
s 只包含小写英文字母
"""


# slow but work


from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @lru_cache
        def f(s):
            if len(s) == 0:
                return 0
            if len(s) == 1:
                return 1
            if s[0] == s[-1]:
                return f(s[1:-1]) + 2
            return max(f(s[1:]), f(s[:-1]))

        return f(s)



from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @lru_cache
        def f(s):
            if len(s) == 0:
                return 0
            if len(s) == 1:
                return 1
            if s[0] == s[-1]:
                return f(s[1:-1]) + 2
            return max(f(s[1:]), f(s[:-1]))

        return f(s)



class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        for row in dp:
            print(row)
        return dp[0][-1]


# 遍历的顺序非常的重要

"""
动态规划，四要素
状态
f[i][j] 表示 s 的第 i 个字符到第 j 个字符组成的子串中，最长的回文序列长度是多少。

转移方程
如果 s 的第 i 个字符和第 j 个字符相同的话

f[i][j] = f[i + 1][j - 1] + 2

如果 s 的第 i 个字符和第 j 个字符不同的话

f[i][j] = max(f[i + 1][j], f[i][j - 1])

然后注意遍历顺序，i 从最后一个字符开始往前遍历，j 从 i + 1 开始往后遍历，这样可以保证每个子问题都已经算好了。

初始化
f[i][i] = 1 单个字符的最长回文序列是 1

结果
f[0][n - 1]

"""



from functools import lru_cache

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @lru_cache
        def f(s):
            length = len(s)
            if length < 2:
                return length
            if s[0] == s[-1]:
                return f(s[1:-1]) + 2
            return max(f(s[1:]), f(s[:-1]))

        return f(s)



class Solution:
    """
    多磨简单的一道题 就是做不出来
    """
    def longestPalindromeSubseq(self, s: str) -> int:
        length = len(s)
        dp = [[0] * (length) for _ in range(length)]
        for i in range(length-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, length):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])

        return dp[0][-1]


if __name__ == '__main__':
    s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
    print(Solution().longestPalindromeSubseq(s))

