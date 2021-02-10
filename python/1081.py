"""
https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


1081. Smallest Subsequence of Distinct Characters
Medium

667

96

Add to List

Share
Return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Note: This question is the same as 316: https://leetcode.com/problems/remove-duplicate-letters/



Example 1:

Input: s = "bcabc"
Output: "abc"
Example 2:

Input: s = "cbacdcbc"
Output: "acdb"


Constraints:

1 <= s.length <= 1000
s consists of lowercase English letters.
"""


from typing import List


class Solution:
    def smallestSubsequence(self, s: str) -> str:
        visited = set()
        stack = []
        for c in s:
            if c in visited:
                continue
            stack.append(c)
            visited.add(c)
        # this will return the first match sequence, not the smallest sequence
        return ''.join(stack)



class Solution:
    """
    exmaple: cac
    """
    def smallestSubsequence(self, s: str) -> str:
        from collections import Counter
        cnt = Counter(s)
        visited = set()
        stack = []
        for c in s:
            cnt[c] -= 1
            if c in visited:
                continue
            while stack and cnt[stack[-1]] > 0 and stack[-1] > c:
                visited.remove(stack.pop())

            visited.add(c)
            stack.append(c)

        return ''.join(stack)



class Solution:
    # 整个思路其实很简单 但是不知道为什么 总是不理解
    # 因为不理解 所以记不住啊
    def removeDuplicateLetters(self, s: str) -> str:
        # 记录每个字符出现的最后的下标
        # 如果一个字符出现了好几次 只记录最后一次
        last_indexes = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            # 如果当前字符已经存在了 就跳过
            if c in stack:
                continue
            # 如果当前字符比栈顶的字符要小
            # 而且栈顶的字符在当前字符的后面还存在 那么就替换掉栈顶的字符
            # 这个过程是递归进行的
            while stack and stack[-1] > c and last_indexes[stack[-1]] > i:
                stack.pop()
            stack.append(c)

        return ''.join(stack)


if __name__ == '__main__':
    s = "bcabc"
    print(Solution().smallestSubsequence(s))

    s = "cbacdcbc"
    print(Solution().smallestSubsequence(s))

