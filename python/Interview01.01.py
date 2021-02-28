"""
https://leetcode-cn.com/problems/is-unique-lcci/

面试题 01.01. 判定字符是否唯一
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false
示例 2：

输入: s = "abc"
输出: true
限制：

0 <= len(s) <= 100
如果你不使用额外的数据结构，会很加分。

"""


class Solution:
    def isUnique(self, astr: str) -> bool:
        return len(set(astr)) == len(astr)


class Solution:
    def isUnique(self, astr: str) -> bool:
        mark = 0

        for c in astr:
            i = ord(c) - ord('a')
            if mark & (1 << i):
                return False
            mark |= 1 << i

        return True


class Solution:
    def isUnique(self, astr: str) -> bool:
        # 如果mask是32位的整数
        # 那么最多有26位被占用 够用了
        mask = 0
        for c in astr:
            i = ord(c) - 67
            if mask & (1 << i):
                return False
            mask |= 1 << i

        return True

