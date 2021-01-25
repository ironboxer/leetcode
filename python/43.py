"""
https://leetcode.com/problems/multiply-strings/

Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return 0

        m, n = len(num1), len(num2)
        pos = [0] * (m + n)
        num1, num2 = num1[::-1], num2[::-1]
        for i in range(m):
            for j in range(n):
                t = int(num1[i]) * int(num2[j])
                x = t % 10
                y = t // 10
                pos[i + j] += x
                pos[i + j + 1] += y
        for i in range(m + n - 1):
            pos[i + 1] += pos[i] // 10
            pos[i] %= 10

        s = ''.join(str(i) for i in pos[::-1])
        return s if s[0] != '0' else s[1:]


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        dp = [0] * (m + n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i+j+1] += int(num1[i]) * int(num2[j])
        carry = 0
        for i in range(m+n-1, -1, -1):
            val = dp[i] + carry
            dp[i] = val % 10
            carry = val // 10
        print(dp)
        return ''.join(str(i) for i in dp).lstrip('0') or '0'


if __name__ == "__main__":
    num1 = "2"
    num2 = "3"
    print(Solution().multiply(num1, num2))

    num1 = "123"
    num2 = "456"
    print(Solution().multiply(num1, num2))
