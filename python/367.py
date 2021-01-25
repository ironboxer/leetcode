"""
https://leetcode.com/problems/valid-perfect-square/


Given a positive integer num, write a function which returns True if num is a perfect square else False.

Follow up: Do not use any built-in library function such as sqrt.



Example 1:

Input: num = 16
Output: true
Example 2:

Input: num = 14
Output: false


Constraints:

1 <= num <= 2^31 - 1

"""


class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num+1):
            v = i ** 2
            if v > num:
                return False
            if v == num:
                return True
        return False


class Solution:
    """
    Newton's Method
    牛顿无聊啊
    """
    def isPerfectSquare(self, num: int) -> bool:
        r = num
        while r ** 2 > num:
            r = (r + num // r) >> 1
        return r ** 2 == num



if __name__ == '__main__':
    for i in range(1, 101):
        print(i, Solution().isPerfectSquare(i))

