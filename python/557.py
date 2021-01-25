"""
https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/

557. 反转字符串中的单词 III
给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。



示例：

输入："Let's take LeetCode contest"
输出："s'teL ekat edoCteeL tsetnoc"


提示：

在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        buf = [c for c in s]
        total = len(buf)

        l = 0
        for i in range(total+1):
            if i == total or buf[i] == ' ':
                r = i - 1
                while l < r:
                    buf[l], buf[r] = buf[r], buf[l]
                    l, r = l + 1, r - 1
                l = i + 1

        return ''.join(buf)


