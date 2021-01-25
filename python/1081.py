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


if __name__ == '__main__':
    s = "bcabc"
    print(Solution().smallestSubsequence(s))

    s = "cbacdcbc"
    print(Solution().smallestSubsequence(s))

