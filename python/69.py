"""
https://leetcode.com/problems/sqrtx/

Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""


# slowly
class Solution1:
    def mySqrt(self, x: int) -> int:
        for i in range(0, x+1):
            v = i ** 2
            if v == x:
                return i
            elif v > x:
                return i - 1


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x // 2
        while l <= r:
            print(l, r)
            m = (l + r) // 2
            v = m ** 2
            if v < x:
                l = m + 1
            elif v > x:
                r = m - 1
            else:
                return m

        return r

# 简单的二分查找

if __name__ == '__main__':
    for i in range(0, 20):
        r = Solution().mySqrt(i)
        print("%s, %s" %  (i, r))

    print(Solution().mySqrt(2147395599))
