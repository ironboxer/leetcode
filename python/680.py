"""
https://leetcode-cn.com/problems/valid-palindrome-ii/

680. 验证回文字符串 Ⅱ
给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。

示例 1:

输入: "aba"
输出: True
示例 2:

输入: "abca"
输出: True
解释: 你可以删除c字符。
注意:

字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def f(s, l, r):
            while l < r and s[l] == s[r]:
                l, r = l + 1, r - 1
            return l >= r

        l, r = 0, len(s) - 1
        # 找到第一组不相等的元素 然后分别 跳过 判断
        while l < r and s[l] == s[r]:
            l, r = l + 1, r - 1
        return f(s, l, r - 1) or f(s, l + 1, r)

