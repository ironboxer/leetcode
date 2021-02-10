"""
https://leetcode.com/problems/remove-duplicate-letters/


Given a string which contains only lowercase letters, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/

"""


class Solution:
    """
    其实很难理解 因为到了后面就记不住了

    这段代码并不是不好 而且超出了当前你自己的理解能力
    有很多看似很简单的点你是不知道的
    就像股票买卖的代码 也是很简单
    可是背后的思考逻辑你就不知道了
    """
    def removeDuplicateLetters(self, s: str) -> str:
        # index保存的是每个字符对应的最靠后的下标
        index = {c: i for i, c in enumerate(s)}
        res = []
        for i, c in enumerate(s):
            print(c, res)
            if c in res:
                continue
            # c 比res[-1]小 而且res[-1]在后面还有
            while res and c < res[-1] and i < index[res[-1]]:
                res.pop()
            res.append(c)

        return ''.join(res)


class Solution:
    """
    something like sliding window
    因为一开始就不会 所以根本记不住

    能够记住的前提就是你理解了它 否则 就没啥用了
    """
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        # counter保证stack在pop的时候不会pop出前面只出现了一次的元素
        cnt = Counter(s)
        # visited保证同一个元素只被加入stack一次
        visited = set()
        stack = []
        for c in s:
            cnt[c] -= 1
            if c in visited:
                continue
            while stack and cnt[stack[-1]] > 0 and stack[-1] > c:
                visited.remove(stack.pop())

            stack.append(c)
            visited.add(c)

        return ''.join(stack)


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_indexes = {c: i for i, c in enumerate(s)}
        stack = []
        for i, c in enumerate(s):
            if c in stack:
                continue
            while stack and stack[-1] > c and last_indexes[stack[-1]] > i:
                stack.pop()
            stack.append(c)

        return ''.join(stack)



if __name__ == '__main__':
    s = "bcabc"
    print(s)
    print(Solution().removeDuplicateLetters(s))

    s = "cbacdcbc"
    print(s)
    print(Solution().removeDuplicateLetters(s))

