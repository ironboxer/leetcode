"""
https://leetcode-cn.com/problems/palindrome-partitioning-ii/v


132. 分割回文串 II
给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回符合要求的最少分割次数。

示例:

输入: "aab"
输出: 1
解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。

"""


from functools import lru_cache


@lru_cache
def check(s):
    l, r = 0, len(s) - 1
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l + 1, r - 1
    return True


class Solution:
    def minCut(self, s: str) -> int:

        @lru_cache
        def f(s):
            if check(s):
                return 0
            res = len(s) - 1
            for i in range(1, len(s)):
                l, r = f(s[:i]), f(s[i:])
                res = min(res, l + r + 1)
            return res

        return f(s)


if __name__ == '__main__':
    cases = [
        ('a', 0),
        ('aab', 1),
        ('ab', 1),
        ('cdd', 1),
        ("abbab", 1),
        ("eegiicgaeadbcfacfhifdgj", 18),
        ("eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj", 42),
    ]

    for s, e in cases:
        t = Solution().minCut(s)
        print(s, e, t)
        assert e == t

