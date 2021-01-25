"""
https://leetcode.com/problems/generate-parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""
#  每一道题都是套路

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def f(s, l, r):
            if len(s) == n * 2:
                res.append(s)
                return

            if l > 0:
                f(s + "(", l - 1, r)
            if l < r:
                f(s + ")", l, r - 1)

        f("", n, n)

        return res


# 为什么呢? 自己的思路永远是错的
# https://leetcode.com/problems/generate-parentheses/discuss/10100/Easy-to-understand-Java-backtracking-solution
# 作者的思路太好了, 一次只添加一个(或者), 如果每次都添加一对(), 则因为corner case太多, 无法穷举

if __name__ == "__main__":
    cases = [
        (4, ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()",
             "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"])
    ]

    for n, r in cases:
        print(n, r)
        t = Solution().generateParenthesis(n)
        try:
            assert r == t
        except AssertionError:
            print(t)
            print(set(r).difference(set(t)))
