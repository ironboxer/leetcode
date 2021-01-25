"""
https://leetcode-cn.com/problems/add-strings/

415. 字符串相加
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。



提示：

num1 和num2 的长度都小于 5100
num1 和num2 都只包含数字 0-9
num1 和num2 都不包含任何前导零
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式

"""


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        res = 0
        t = 0
        i, j = len(num1) - 1, len(num2) - 1
        k = 0

        while i >= 0 and j >= 0:
            r = int(num1[i]) + int(num2[j]) + t
            v, t = r % 10, r // 10
            res = res + v * (10 ** k)
            i, j = i - 1, j - 1
            k += 1

        while i >= 0:
            r = int(num1[i]) + t
            v, t = r % 10, r // 10
            res = res + v * (10 ** k)
            i -= 1
            k += 1

        while j >= 0:
            r = int(num2[j]) + t
            v, t = r % 10, r // 10
            res = res + v * (10 ** k)
            j -= 1
            k += 1

        if t:
            res = res + t * (10 ** k)

        return str(res)


if __name__ == '__main__':
    print(Solution().addStrings("1", "9"))

