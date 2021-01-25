"""
https://leetcode.com/problems/bitwise-and-of-numbers-range/

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all numbers in this range, inclusive.

Example 1:

Input: [5,7]
Output: 4
Example 2:

Input: [0,1]
Output: 0


The idea is very simple:

last bit of (odd number & even number) is 0.
when m != n, There is at least an odd number and an even number, so the last bit position result is 0.
Move m and n rigth a position.
Keep doing step 1,2,3 until m equal to n, use a factor to record the iteration time.

"""


class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        steps = 0
        while n != m:
            m >>= 1
            n >>= 1
            steps += 1

        return m << steps

#  这道题没有看懂是啥


if __name__ == '__main__':
    print(Solution().rangeBitwiseAnd(5, 7))
    print(Solution().rangeBitwiseAnd(0, 1))
