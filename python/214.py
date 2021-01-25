"""
https://leetcode.com/problems/shortest-palindrome/

Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"

Example 2:

Input: "abcd"
Output: "dcbabcd"

"""

class Solution:
    """
    KMP is good, but it's too complicated to understand
    Also, if you try your best, you can do it.
    """
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s) + 1):
            print(s, r[i:], s.startswith(r[i:]))
            # 稍微想一下 其实很简单
            # 就是一个简单的翻转对称
            if s.startswith(r[i:]):
                return r[:i] + s


if __name__ == '__main__':
    print(Solution().shortestPalindrome("abcdefg"))
    print(Solution().shortestPalindrome("aacecaaa"))
    print(Solution().shortestPalindrome("abcd"))

