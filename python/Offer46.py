"""
https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/


剑指 Offer 46. 把数字翻译成字符串
给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。



示例 1:

输入: 12258
输出: 5
解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"


提示：

0 <= num < 231
"""


from functools import lru_cache

class Solution:
    def translateNum(self, num: int) -> int:
        s = str(num)
        ops = list(map(str, range(26)))

        @lru_cache
        def f(s):
            if not s:
                return 1
            r = 0
            for op in ops:
                if op == s[:len(op)]:
                    r += f(s[len(op):])
            return r

        return f(s)
