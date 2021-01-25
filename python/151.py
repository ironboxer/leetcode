"""
https://leetcode-cn.com/problems/reverse-words-in-a-string/

151. 翻转字符串里的单词
给定一个字符串，逐个翻转字符串中的每个单词。

说明：

无空格字符构成一个 单词 。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。


示例 1：

输入："the sky is blue"
输出："blue is sky the"
示例 2：

输入："  hello world!  "
输出："world! hello"
解释：输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
示例 3：

输入："a good   example"
输出："example good a"
解释：如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
示例 4：

输入：s = "  Bob    Loves  Alice   "
输出："Alice Loves Bob"
示例 5：

输入：s = "Alice does not even like bob"
输出："bob like even not does Alice"


提示：

1 <= s.length <= 104
s 包含英文大小写字母、数字和空格 ' '
s 中 至少存在一个 单词


进阶：

请尝试使用 O(1) 额外空间复杂度的原地解法。
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        import re
        return ' '.join(re.findall(r'[\S]+', s)[::-1])


class Solution:
    def reverseWords(self, s: str) -> str:
        buf = []
        l, r = 0, len(s) - 1
        while s[l] == ' ':
            l += 1
        while s[r] == ' ':
            r -= 1
        while l <= r:
            i = r
            while l <= i and s[i] != ' ':
                i -= 1
            buf.append(s[i+1:r+1])
            while l <= i and s[i] == ' ':
                i -= 1
            r = i
        return ' '.join(buf)


# follow up: 如果面试官说 内存不够 放不下 怎么办
# 这种情况下只能返回一个生成器 你自己迭代写到磁盘或者IO吧
# 反正是一个字符串的流
class Solution2:
    def reverseWords(self, s: str) -> str:
        l, r = 0, len(s) - 1
        while s[l] == ' ':
            l += 1
        while s[r] == ' ':
            r -= 1
        first = True
        while l <= r:
            i = r
            while l <= i and s[i] != ' ':
                i -= 1
            if first:
                first = False
            else:
                yield ' '
            yield s[i+1:r+1]
            while l <= i and s[i] == ' ':
                i -= 1
            r = i


if __name__ == '__main__':
    cases = [
        ("the sky is blue", "blue is sky the"),
        ("  hello world!  ", "world! hello"),
        ("a good   example", "example good a"),
        ("  Bob    Loves  Alice   ", "Alice Loves Bob"),
        ("Alice does not even like bob", "bob like even not does Alice"),
    ]

    for a, b in cases:
        r = Solution().reverseWords(a)
        print("%s|%s|%s" % (a, b, r))
        assert b == r

    for a, b in cases:
        r = Solution2().reverseWords(a)
        r = ''.join(r)
        print("%s|%s|%s" % (a, b, r))
        assert b == r
