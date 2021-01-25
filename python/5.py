"""
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # "babad"
        res, N = "", len(s)
        for i in range(N):
            left, right = i, i
            while left >= 0 and right < N:
                if s[left] != s[right]:
                    break
                left, right = left - 1, right + 1
            if right - left - 1 > len(res):
                res = s[left+1: right]
            if i + 1 < N and s[i] == s[i+1]:
                left, right = i, i + 1
                while left >= 0 and right < N:
                    if s[left] != s[right]:
                        break
                    left, right = left - 1, right + 1
                if right - left - 1 > len(res):
                    res = s[left+1: right]
        return res


if __name__ == "__main__":
    print(Solution().longestPalindrome("babad"))
