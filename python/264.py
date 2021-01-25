"""
https://leetcode.com/problems/ugly-number-ii/

Write a program to find the n-th ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Example:

Input: n = 10
Output: 12
Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note:

1 is typically treated as an ugly number.
n does not exceed 1690.

"""


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        a = b = c = 0
        while len(res) < n:
            while res[a] * 2 <= res[-1]:
                a += 1
            while res[b] * 3 <= res[-1]:
                b += 1
            while res[c] * 5 <= res[-1]:
                c += 1
            res.append(min(res[a] * 2, res[b] * 3, res[c] * 5))

        return res[-1]


if __name__ == '__main__':
    for i in range(1, 100):
        print(i, Solution().nthUglyNumber(i))


