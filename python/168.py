"""
https://leetcode.com/problems/excel-sheet-column-title/

Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

"""


class Solution:
    def convertToTitle(self, n: int) -> str:
        maps = {i: chr(65 + i) for i in range(26)}
        res = []
        while n:
            r = (n-1) % 26
            res.append(maps[(r + 26) % 26])
            n = (n - 1) // 26
        return ''.join(res[::-1])

#  被这种破题给困住了


if __name__ == '__main__':
    for i in range(1, 100):
        print(i, Solution().convertToTitle(i))
    print(Solution().convertToTitle(701))