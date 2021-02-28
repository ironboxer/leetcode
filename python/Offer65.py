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
        mask = (1 << 32) - 1
        a, b = a & mask, b & mask
        while b:
            a, b = (a ^ b) & mask, (a & b) << 1 & mask

        return a if a <= mask >> 1 else ~(a ^ mask)


class Solution:
    def add(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return a if b == 0 else b

        s, carry = 0, 0
        while b:
            # 只相加不进位
            s = a ^ b
            # 只算进位
            carry = (a & b) << 1
            a, b = s, carry

        return a

"""
# go 运行的的确很快 因为直接编译成了机器码了
没有虚拟机
func add(a int, b int) int {
    if a == 0 {
        return b
    }
    if b == 0 {
        return a
    }
    var sum = 0
    var carry = 0
    for b != 0 {
        sum = a ^ b
        carry = (a & b) << 1
        a = sum
        b = carry
    }
    return a
}
"""
