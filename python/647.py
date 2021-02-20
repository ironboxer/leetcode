"""
https://leetcode-cn.com/problems/palindromic-substrings/

647. 回文子串
给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。



示例 1：

输入："abc"
输出：3
解释：三个回文子串: "a", "b", "c"
示例 2：

输入："aaa"
输出：6
解释：6个回文子串: "a", "a", "a", "aa", "aa", "aaa"


提示：

输入的字符串长度不会超过 1000 。
"""


from functools import lru_cache


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        def f(s, l, r):
            nonlocal res
            while l >= 0 and r < len(s):
                if s[l] != s[r]:
                    break
                res += 1
                l, r = l - 1, r + 1
            return res

        for i in range(len(s)):
            f(s, i, i)
            f(s, i, i+1)

        return res



class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0

        dp = [[0] * n for _ in range(n)]

        for r in range(n):
            for l in range(r+1):
                if l == r:
                    dp[l][r] = True
                    res += 1
                elif l + 1 == r and s[l] == s[r]:
                    dp[l][r] = True
                    res += 1
                elif dp[l+1][r-1] and s[l] == s[r]:
                    dp[l][r] = True
                    res += 1

        return res


class Solution:
    def countSubstrings(self, s: str) -> int:
        retval = 0
        total = len(s)
        # dp用来维持状态 retval用来记录结果
        dp = [[False] * total for _ in range(total)]
        # right border
        for r in range(total):
            # left border
            for l in range(r+1):
                # left == right only one element itself
                if l == r:
                    retval += 1
                    dp[l][r] = True
                # l r 中间间隔一个元素 同时s[l] == s[r] 这里无法使用dp[i][j]之间的公式来得出
                # 这就是一种基本的情况 不需要状态转移方程得到
                elif l + 1 == r and s[l] == s[r]:
                    retval += 1
                    dp[l][r] = True
                # 需要使用状态转移方程的情况
                elif dp[l+1][r-1] and s[l] == s[r]:
                    retval += 1
                    dp[l][r] = True

        return retval



if __name__ == '__main__':
    s = "abc"
    print(s)
    print(Solution().countSubstrings(s))

    s = "aaa"
    print(s)
    print(Solution().countSubstrings(s))


