"""
https://leetcode.com/problems/word-break/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false

"""

from typing import List


class Solution0:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        def f(string):
            if not string:
                return True
            for w in wordDict:
                if string.startswith(w):
                    r = f(string[len(w):])
                    if r:
                        return True

            return False

        return f(s)


# 递归超时的版本

class Solution0:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        memo = {}

        def f(i):
            if i == n:
                return True
            if i in memo:
                return memo[i]
            for w in wordDict:
                if i + len(w) <= n and s[i:i + len(w)] == w:
                    r = f(i + len(w))
                    if r:
                        memo[i] = True
                        return True
            memo[i] = False
            return False

        return f(0)


# 递归+memo的版本和动态规划的版本其实已经很接近了
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict.sort(key=lambda x: len(x))
        n = len(s)
        dp = [False] * (n + 1)
        # is s is empty, then return true
        dp[0] = True
        for i in range(1, n + 1):
            for w in wordDict:
                if i - len(w) >= 0:
                    if s[i - len(w):i] == w and dp[i - len(w)]:
                        dp[i] = True
                        break
                else:
                    break
        return dp[n]


# 和递归的版本是一模一样的, 只是减少了栈的空间, 增加了堆的空间


if __name__ == '__main__':
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(Solution().wordBreak(s, wordDict))

    s = "applepenapple"
    wordDict = ["apple", "pen"]
    print(Solution().wordBreak(s, wordDict))

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(Solution().wordBreak(s, wordDict))

    s = "cars"
    wordDict = ["car", "ca", "rs"]
    print(Solution().wordBreak(s, wordDict))

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print(Solution().wordBreak(s, wordDict))
