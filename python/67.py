"""
https://leetcode.com/problems/add-binary/

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

Each string consists only of '0' or '1' characters.
1 <= a.length, b.length <= 10^4
Each string is either "0" or doesn't contain any leading zero.
"""

# 麻烦但是很简单

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = a[::-1], b[::-1]
        m, n = len(a), len(b)
        i, j = 0, 0
        v = 0
        res = []
        while i < m and j < n:
            r = int(a[i]) + int(b[j]) + v
            res.append(r % 2)
            v = r // 2
            i, j = i + 1, j + 1

        while i < m:
            r = int(a[i]) + v
            res.append(r % 2)
            v = r // 2
            i += 1
        while j < n:
            r = int(b[j]) + v
            res.append(r % 2)
            v = r // 2
            j += 1

        if v:
            res.append(v)

        return ''.join([str(i) for i in res[::-1]])



if __name__ == '__main__':
    pass

