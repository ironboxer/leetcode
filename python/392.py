"""
https://leetcode-cn.com/problems/is-subsequence/

392. 判断子序列
给定字符串 s 和 t ，判断 s 是否为 t 的子序列。

字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。

进阶：

如果有大量输入的 S，称作 S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T 的子序列。在这种情况下，你会怎样改变代码？

致谢：

特别感谢 @pbrother 添加此问题并且创建所有测试用例。



示例 1：

输入：s = "abc", t = "ahbgdc"
输出：true
示例 2：

输入：s = "axc", t = "ahbgdc"
输出：false


提示：

0 <= s.length <= 100
0 <= t.length <= 10^4
两个字符串都只由小写字符组成。

"""



class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[False] * (n + 1) for i in range(m + 1)]
        dp[0][0] = True
        for i in range(m):
            for j in range(n):
                if s[i] == t[j]:
                    dp[i+1][j+1] = dp[i][j]
                else:
                    dp[i+1][j+1] = dp[i+1][j]


        return dp[m][n]




# Slow but Work
from functools import lru_cache


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        @lru_cache
        def f(s, t):
            if not s:
                return True
            if not t:
                return not s
            if s[0] == t[0]:
                return f(s[1:], t[1:])
            return f(s, t[1:])


        return f(s, t)




# 标准的DP做法
# 应该还有可以优化的空间
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        dp = [[False] * (n + 1) for _ in range(m+1)]
        for i in range(n+1):
            dp[m][i] = True
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = dp[i][j+1]
        return dp[0][0]





# 这才是最好的解法 简单而且高效 而且切题
# 其他的方法都是不好的
# 双指针的方法 two pointer

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        i, j = 0, 0
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == m


if __name__ == '__main__':
    s = "axc"
    t = "ahbgdc"

    print(s, t)
    print(Solution().isSubsequence(s, t))

    s = "abc"
    t = "ahbgdc"

    print(s, t)
    print(Solution().isSubsequence(s, t))




