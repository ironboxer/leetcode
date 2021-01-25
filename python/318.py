"""
https://leetcode.com/problems/maximum-product-of-word-lengths/


Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:

Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:

Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:

Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.

"""

from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_len = 0
        s = {i: set(w) for i, w in enumerate(words)}
        total = len(words)
        for i in range(total):
            for j in range(i + 1, total):
                if not s[i].intersection(s[j]):
                    max_len = max(max_len, len(words[i]) * len(words[j]))

        return max_len


if __name__ == '__main__':
    words = ["abcw","baz","foo","bar","xtfn","abcdef"]
    print(Solution().maxProduct(words))

    words = ["a","ab","abc","d","cd","bcd","abcd"]
    print(Solution().maxProduct(words))

    words = ["a","aa","aaa","aaaa"]
    print(Solution().maxProduct(words))

    words = ["eae","ea","aaf","bda","fcf","dc","ac","ce","cefde","dabae"]
    print(Solution().maxProduct(words))

