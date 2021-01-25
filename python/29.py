"""
https://leetcode.com/problems/divide-two-integers

Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX = 2 ** 31
        a, b = dividend, divisor
        if a == 0:
            return 0
        if b == 0:
            return MAX - 1
        if a < 0 and b < 0 or a > 0 and b > 0:
            sign = 1
        else:
            sign = -1
        a, b = abs(a), abs(b)
        res = 0
        # 最核心的 但是看不懂的地方
        while a >= b:
            i = 0
            while a >= b << (i+1):
                i += 1
            res += 1 << i
            a -= b << i

        if sign == 1:
            return min(MAX-1, res)
        return MAX - 1 if res > MAX else -res

#这是一道不会的题
#位操作很迷茫
# 没有看题解

"""
 /**
     * 解题思路：这题是除法，所以先普及下除法术语
     * 商，公式是：(被除数-余数)÷除数=商，记作：被除数÷除数=商...余数，是一种数学术语。
     * 在一个除法算式里，被除数、余数、除数和商的关系为：(被除数-余数)÷除数=商，记作：被除数÷除数=商...余数，
     * 进而推导得出：商×除数+余数=被除数。
     *
     * 要求商，我们首先想到的是减法，能被减多少次，那么商就为多少，但是明显减法的效率太低
     *
     * 那么我们可以用位移法，因为计算机在做位移时效率特别高，向左移1相当于乘以2，向右位移1相当于除以2
     *
     * 我们可以把一个dividend（被除数）先除以2^n，n最初为31，不断减小n去试探,当某个n满足dividend/2^n>=divisor时，
     *
     * 表示我们找到了一个足够大的数，这个数*divisor是不大于dividend的，所以我们就可以减去2^n个divisor，以此类推
     *
     * 我们可以以100/3为例
     *
     * 2^n是1，2，4，8...2^31这种数，当n为31时，这个数特别大，100/2^n是一个很小的数，肯定是小于3的，所以循环下来，
     *
     * 当n=5时，100/32=3, 刚好是大于等于3的，这时我们将100-32*3=4，也就是减去了32个3，接下来我们再处理4，同样手法可以再减去一个3
     *
     * 所以一共是减去了33个3，所以商就是33
     *
     * 这其中得处理一些特殊的数，比如divisor是不能为0的，Integer.MIN_VALUE和Integer.MAX_VALUE
     *
     */
"""

# a better solution
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 1 << 31
        if dividend == 0:
            return 0
        if dividend == -MAX_INT and divisor == -1:
            return MAX_INT - 1
        neg = bool((dividend ^ divisor) < 0)
        t, d = abs(dividend), abs(divisor)
        res = 0
        # 为什么是这样的
        for i in range(31, -1, -1):
            if (t >> i) >= d:
                res += 1 << i
                t -= d << i

        return -res if neg else res


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 1 << 31
        if dividend == 0:
            return 0
        if dividend == -MAX_INT and divisor == -1:
            return MAX_INT - 1
        neg = -1 if (dividend ^ divisor) < 0 else 1
        a, b, res = abs(dividend), abs(divisor), 0
        for i in range(31, -1, -1):
            # 因为不让用* 所以需要变形
            if a >= b * (1 << i):
                a -= b * (1 << i)
                res += 1 << i

        return neg * res



if __name__ == "__main__":
    print(Solution().divide(10, 3))
    print(Solution().divide(7, -3))


