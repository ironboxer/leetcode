"""
https://leetcode.com/problems/word-pattern/


Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

bijection: 双射

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false
"""

class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        P, S = [c for c in pattern], str.split(' ')
        if len(P) != len(S):
            return False
        A, B = {}, {}
        for i, j in zip(P, S):
            if i in A and A[i] != j:
                return False
            if j in B and B[j] != i:
                return False
            A[i] = j
            B[j] = i

        return True


if __name__ == '__main__':
     pattern = "abba"
     str = "dog cat cat dog"
     print(Solution().wordPattern(pattern, str))

     pattern = "abba"
     str = "dog cat cat fish"
     print(Solution().wordPattern(pattern, str))

     pattern = "aaaa"
     str = "dog cat cat dog"
     print(Solution().wordPattern(pattern, str))

     pattern = "abba"
     str = "dog dog dog dog"
     print(Solution().wordPattern(pattern, str))

