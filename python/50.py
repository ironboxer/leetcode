"""
https://leetcode.com/problems/powx-n/

Implement pow(x, n), which calculates x raised to the power n (i.e. xn).

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
-104 <= xn <= 104

"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        res = 1.0
        while n:
            if n & 1:
                res *= x
            x = x * x
            # 这个地方不能用 x ** 2, 不知道为什么, 应该属于Python的一个bug
            # print("T", x * x, x ** 2)
            n >>= 1
        return res


# 你真逗明白了吗?
# 数值计算这里, 是一个弱项

if __name__ == "__main__":
    cases = [
        (2.0, 10, 1024.0),
        (2.1, 3, 9.261),
        (2.0, -2, 0.25),
        (0.00001, 2147483647, 0),
        (2.00000, -2147483648, 0),
    ]
    for x, n, t in cases:
        r = Solution().myPow(x, n)
        print(x, n, t, r)
        assert abs(t - r) < 0.00001
