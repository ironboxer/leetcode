"""
https://leetcode.com/problems/power-of-two/

Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true
Explanation: 20 = 1

Example 2:

Input: 16
Output: true
Explanation: 24 = 16

Example 3:

Input: 218
Output: false

"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        for i in range(32):
            v = 1 << i
            if v == n:
                return True
            if v > n:
                break
        return False


if __name__ == '__main__':
    print(Solution().isPowerOfTwo(1))
    print(Solution().isPowerOfTwo(16))
    print(Solution().isPowerOfTwo(218))
