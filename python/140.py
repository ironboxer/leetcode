"""
https://leetcode.com/problems/word-break-ii/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]

"""

from typing import List


class Solution0:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        n = len(s)
        wordDict.sort(key=lambda x: len(x))

        def f(i, buf):
            if i == n:
                res.append(' '.join(buf))
                return
            for w in wordDict:
                if i + len(w) <= n:
                    if s[i: i + len(w)] == w:
                        buf.append(w)
                        f(i + len(w), buf)
                        buf.pop()
                else:
                    break

        f(0, [])
        return res


# 超时的版本

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        memo = {}

        def f(string):
            # cache
            if len(string) in memo:
                return memo[len(string)]
            res = []
            for word in wordDict:
                if string.startswith(word):
                    # whole match
                    if len(string) == len(word):
                        res.append([word])
                    else:
                        # partial match
                        res.extend([word] + items for items in f(string[len(word):]))
                        # items = f(string[len(word):])
                        # for item in items:
                        #     res.append([word] + item)
            memo[len(string)] = res
            return res

        r = f(s)
        return [' '.join(items) for items in r]


# 这个算法的本周的思考的逻辑你懂不?





# slow but work
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []

        def f(s, buf):
            if not s:
                res.append(buf[:])
                return

            for word in wordDict:
                if s.startswith(word):
                    buf.append(word)
                    f(s[len(word):], buf)
                    buf.pop()

        f(s, [])

        return [' '.join(item) for item in res]




from functools import lru_cache


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        @lru_cache
        def f(s):
            res = []
            for word in wordDict:
                if s.startswith(word):
                    # 这里很重要 涉及到判空的处理
                    # 如果直接返回一个[]不知道前面的有没有匹配上
                    if s == word:
                        res.append([word])
                        continue
                    buf = f(s[len(word):])
                    items = [[word] + item for item in buf]
                    res.extend(items)
            return res

        return [' '.join(item) for item in f(s)]


from functools import lru_cache


# 写的次数越多 思路越一致

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        @lru_cache
        def f(s):
            if not s:
                return []
            res = []
            for word in wordDict:
                if s == word:
                    res.append([word])
                elif s.startswith(word):
                    buf = f(s[len(word):])
                    res += [[word] + items for items in buf]

            return res

        return [' '.join(items) for items in f(s)]



if __name__ == '__main__':
    s = "catsanddog"
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    print(Solution().wordBreak(s, wordDict))
    import sys
    sys.exit(0)
    s = "pineapplepenapple"
    wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    print(Solution().wordBreak(s, wordDict))

    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(Solution().wordBreak(s, wordDict))

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
    wordDict = ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"]
    print(Solution().wordBreak(s, wordDict))
