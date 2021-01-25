"""
https://leetcode-cn.com/problems/basic-calculator-iii/

772. 基本计算器 III
实现一个基本的计算器来计算简单的表达式字符串。

表达式字符串只包含非负整数， +, -, *, / 操作符，左括号 ( ，右括号 )和空格 。整数除法需要向下截断。

你可以假定给定的字符串总是有效的。所有的中间结果的范围为 [-2147483648, 2147483647]。

进阶：你可以在不使用内置库函数的情况下解决此问题吗？



示例 1：

输入：s = "1 + 1"
输出：2
示例 2：

输入：s = " 6-4 / 2 "
输出：4
示例 3：

输入：s = "2*(5+5*2)/3+(6/2+8)"
输出：21
示例 4：

输入：s = "(2+6* 3+5- (3*14/7+2)*5)+3"
输出：-12
示例 5：

输入：s = "0"
输出：0


提示：

1 <= s <= 104
s 由整数、'+'、'-'、'*'、'/'、'('、')' 和 ' ' 组成
s 是一个 有效的 表达式
"""


from collections import deque
import re

def f(stack):
    if not stack:
        return 0
    ops, nums = deque(), deque()
    for c in stack:
        if c in ('+', '-', '*', '/'):
            ops.append(c)
        else:
            nums.append(c)
    # print(stack, ops, nums)
    res = 0
    while ops:
        a = nums.popleft()
        b = nums.popleft()
        op = ops.popleft()
        if op in ('*', '/'):
            if op == '*':
                c = a * b
            else:
                sign = 1 if a > 0 and b > 0 or a < 0 and b < 0 else -1
                c = abs(a) // abs(b) * sign
            # print(op, a, b, c)
            nums.appendleft(c)
        elif op in ('+', '-'):
            if ops and ops[0] in ('*', '/'):
                op1 = ops.popleft()
                c = nums.popleft()
                if op1 == '*':
                    d = b * c
                else:
                    sign = 1 if b > 0 and c > 0 or b < 0 and c < 0 else -1
                    d = abs(b) // abs(c) * sign
                nums.appendleft(d)
                nums.appendleft(a)
                ops.appendleft(op)
            else:
                if op == '+':
                    c = a + b
                else:
                    c = a - b
                nums.appendleft(c)
    # print(nums)
    return nums.popleft()


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        tokens = re.findall(r'[+/*()-]|\d+', s)
        for t in tokens:
            if t in ('+', '-', '*', '/', '('):
                stack.append(t)
            elif t == ')':
                j = len(stack) - 1
                while j >= 0 and stack[j] != '(':
                    j -= 1
                r = f(stack[j+1:])
                stack = stack[:j]
                stack.append(r)
            else:
                stack.append(int(t))

        return f(stack)

