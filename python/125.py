"""
https://leetcode.com/problems/valid-palindrome/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        buf = []
        for c in s:
            v = ord(c)
            if 48 <= v <= 57:
                buf.append(c)
            elif 65 <= v <= 90:
                buf.append(chr(v + 32))
            elif 97 <= v <= 122:
                buf.append(c)

        l, r = 0, len(buf) - 1
        while l < r:
            if buf[l] != buf[r]:
                return False
            l, r = l + 1, r - 1
        return True

# 过了

if __name__ == '__main__':
    print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
    print(Solution().isPalindrome("race a car"))
    print(Solution().isPalindrome("0P"))
