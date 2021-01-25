"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        sc = Counter(s)
        tc = Counter(t)
        if len(sc) != len(tc):
            return False
        for c in s:
            if sc[c] != tc[c]:
                return False
        return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print(Solution().isAnagram(s, t))

    s = "rat"
    t = "car"
    print(Solution().isAnagram(s, t))


