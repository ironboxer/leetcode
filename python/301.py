"""
https://leetcode.com/problems/remove-invalid-parentheses/

Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]


https://leetcode.com/problems/remove-invalid-parentheses/discuss/75027/Easy-Short-Concise-and-Fast-Java-DFS-3-ms-solution

"""

from typing import List


class Solution:
    """
    这个算法其实很复杂了 超出了对他的理解
    """
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def remove(s, ans, last_i, last_j, par):
            stack = 0
            for i in range(last_i, len(s)):
                if s[i] == par[0]:
                    stack += 1
                if s[i] == par[1]:
                    stack -= 1
                if stack >= 0:
                    continue
                for j in range(last_j, i+1):
                    if s[j] == par[1] and (j == last_j or s[j-1] != par[1]):
                        remove(s[:j] + s[j+1:], ans, i, j, par)
                return

            rev = s[::-1]
            if par[0] == '(':
                remove(rev, ans, 0, 0, [')', '('])
            else:
                ans.append(rev)

        ans = []
        remove(s, ans, 0, 0, ['(', ')'])
        return ans


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def check(s):
            i = 0
            for c in s:
                if c == '(':
                    i += 1
                elif c == ')':
                    i -= 1
                if i < 0:
                    return False
            return i == 0


        level = {s}
        while True:
            valid = list(filter(check, level))
            if valid:
                return valid
            next_level = set()
            for item in level:
                for i in range(len(item)):
                    if item[i] in '()':
                        next_level.add(item[:i] + item[i+1:])
            level = next_level



if __name__ == '__main__':
    s = "()())()"
    print(Solution().removeInvalidParentheses(s))

    s = "(a)())()"
    print(Solution().removeInvalidParentheses(s))

