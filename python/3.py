"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_val, memo = 0, {}
        for i, e in enumerate(s):
            j = memo.get(e, -1)
            if j == -1:
                memo[e] = i
            else:
                memo = {}
                for k in range(j+1, i+1):
                    memo[s[k]] = k
            max_val = max(max_val, len(memo))
        return max_val

# a Better Solution

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, last, memo = 0, 0, {}
        for i, e in enumerate(s):
            p = memo.get(e)
            if p is not None:
                # 这里 i - last 实际上是 计算这个的长度 len(s[last:i])
                res = max(res, i - last)
                last = max(last, p+1)
            memo[e] = i
            # res = max(res, i - last)
        # len(s) - last 实际上是为了减少 res = max(res, i - last) 这个计算的次数
        return max(res, len(s) - last)



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        memo = {}
        res, lasti = 0, 0
        for i, c in enumerate(s):
            j = memo.get(c)
            if j is not None:
                res = max(res, i - lasti)
                # NOTE: a b b a 需要作比较才能知道lasti是否应该更新
                lasti = max(lasti, j + 1)
            memo[c] = i

        return max(res, len(s) - lasti)


























class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, k = 0, 0
        window = {}
        for i, c in enumerate(s):
            j = window.get(c, -1)
            if j != -1:
                while k <= j:
                    window.pop(s[k])
                    k += 1
            window[c] = i
            res = max(res, len(window))

        return res



if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("loddktdji"))
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution().lengthOfLongestSubstring("bbbbb"))
    print(Solution().lengthOfLongestSubstring("pwwkew"))
    print(Solution().lengthOfLongestSubstring(""))

