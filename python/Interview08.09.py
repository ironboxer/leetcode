"""
https://leetcode-cn.com/problems/bracket-lcci/

面试题 08.09. 括号
括号。设计一种算法，打印n对括号的所有合法的（例如，开闭一一对应）组合。

说明：解集不能包含重复的子集。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def f(i, j, s):
            if n * 2 == len(s):
                res.append(s)
                return
            if i < n:
                f(i+1, j, s + "(")
            if j < i:
                f(i, j+1, s + ")")

        f(0, 0, "")

        return res

