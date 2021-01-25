"""
https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/


剑指 Offer 65. 不用加减乘除做加法
写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。



示例:

输入: a = 1, b = 1
输出: 2


提示：

a, b 均可能是负数或 0
结果不会溢出 32 位整数
"""


class Solution:
    def add(self, a: int, b: int) -> int:
        mask = (1 << 31) - 1
        a, b = a & mask, b & mask
        while b:
            a, b = (a ^ b) & mask, (a & b) << 1 & mask

        return a if a <= mask >> 1 else ~(a ^ mask)

