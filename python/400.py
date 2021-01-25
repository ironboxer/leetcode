"""
https://leetcode-cn.com/problems/nth-digit/


400. 第 N 位数字
在无限的整数序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...中找到第 n 位数字。



注意：n 是正数且在 32 位整数范围内（n < 231）。



示例 1：

输入：3
输出：3
示例 2：

输入：11
输出：0
解释：第 11 位数字在序列 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... 里是 0 ，它是 10 的一部分。
"""


class Solution:
    def findNthDigit(self, n: int) -> int:
        num = 9
        cnt = 1

        while n > num * cnt:
            n -= num * cnt
            num *= 10
            cnt += 1

        target = num // 9 + (n - 1) // cnt
        index = (n - 1) % cnt
        print(num, cnt, n, target, index)
        return str(target)[index]


if __name__ == '__main__':
    for i in range(22):
        print(i, Solution().findNthDigit(i))

