"""
https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof/

剑指 Offer 38. 字符串的排列
输入一个字符串，打印出该字符串中字符的所有排列。



你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。



示例:

输入：s = "abc"
输出：["abc","acb","bac","bca","cab","cba"]


限制：

1 <= s 的长度 <= 8
"""

from typing import List

class Solution:
    def permutation(self, s: str) -> List[str]:
        res = []
        nums = [n for n in s]
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        def f(buf):
            if len(buf) == len(nums):
                res.append(''.join(buf))
                return
            for n in freq:
                if freq[n] > 0:
                    freq[n] -= 1
                    buf.append(n)
                    f(buf)
                    buf.pop()
                    freq[n] += 1

        f([])

        return res


if __name__ == '__main__':
    s = 'aab'
    print(Solution().permutation(s))
