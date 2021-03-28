"""
https://leetcode.com/problems/reverse-integer/

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
过程有点曲折
"""


class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return x
        if x < 0:
            sign = -1
            x = -x
        else:
            sign = 1

        while x % 10 == 0:
            x //= 10

        r = 0
        while x:
            r = r * 10 + x % 10
            x //= 10

        if sign == -1 and r > 2 ** 31:
            return 0
        if sign == 1 and r >= 2 ** 31:
            return 0

        return sign * r


class Solution:
    """
    简单 精巧
    """
    def reverse(self, x: int) -> int:
        max_val = 1 << 31

        sign = 1 if x >= 0 else -1
        x = abs(x)
        r = 0
        while x:
            r = r * 10 + x % 10
            x //= 10
        # print(r)
        if sign == 1:
            return r if r < max_val else 0
        return -r if r <= max_val else 0



if __name__ == "__main__":
    print(Solution().reverse(123))
