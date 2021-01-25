"""
https://leetcode.com/problems/decode-string/

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].



Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
Example 4:

Input: s = "abc3[cd]xyz"
Output: "abccdcdcdxyz"

"""

class Solution:
    """
    这段代码肯定是抄的别人的
    现在居然看不懂!!!
    """
    def decodeString(self, s):
        stack = []
        n = 0
        res = ''
        for c in s:
            if c == '[':
                stack.append(res)
                stack.append(n)
                res = ''
                n = 0
            elif c == ']':
                m = stack.pop()
                q = stack.pop()
                res = q + res * m
            elif c.isdigit():
                n = n * 10 + int(c)
            else:
                res += c

        return res

# 有一个简单的抽象或者说有一个简单的公式: result = preString +  curString * n
# stack则是用来解决嵌套问题的


def tokenize(string):
    tokens = []
    n = ''
    s = ''
    for c in string:
        if c == '[':
            if n:
                tokens.append(int(n))
                n = ''
            tokens.append(c)
        elif c == ']':
            if s:
                tokens.append(s)
                s = ''
            tokens.append(c)
        elif c.isdigit():
            if s:
                tokens.append(s)
                s = ''
            n += c
        else:
            s += c
    if s:
        tokens.append(s)
        s = ''

    return tokens


class Solution:
    """
    还是看不懂 只能尝试着来理解
    """
    def decodeString(self, s: str) -> str:
        tokens = tokenize(s)
        stack = []
        res, n = '', 0
        for token in tokens:
            if token == '[':
                stack.append(res)
                stack.append(n)
                res = ''
                n = 0
            elif token == ']':
                m = stack.pop()
                q = stack.pop()
                res = q + res * m
            elif isinstance(token, int):
                n = token
            else:
                res += token
        
        return res


if __name__ == '__main__':
    cases = [
        ("3[a]2[bc]", "aaabcbc"),
        ("3[a2[c]]", "accaccacc"),
        ("2[abc]3[cd]ef", "abcabccdcdcdef"),
        ("abc3[cd]xyz", "abccdcdcdxyz"),
    ]
    for a, b in cases:
        c = Solution().decodeString(a)
        print(a, b, c)
        assert b == c

