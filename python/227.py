"""
https://leetcode.com/problems/basic-calculator-ii/

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:

Input: "3+2*2"
Output: 7
Example 2:

Input: " 3/2 "
Output: 1
Example 3:

Input: " 3+5 / 2 "
Output: 5
Note:

You may assume that the given expression is always valid.
Do not use the eval built-in library function.

"""


class Solution:
    def calculate(self, s: str) -> int:
        from collections import deque
        nums = deque()
        ops = deque()
        buf = []
        for ch in s:
            if ch == ' ':
                if buf:
                    nums.append(int(''.join(buf)))
                    buf = []
            elif ch in ('+', '-', '*', '/'):
                ops.append(ch)
                if buf:
                    nums.append(int(''.join(buf)))
                    buf = []
            else:
                buf.append(ch)
        if buf:
            nums.append(int(''.join(buf)))
        print(ops)
        print(nums)
        while ops:
            op = ops.popleft()
            a = nums.popleft()
            b = nums.popleft()
            if op in ('+', '-') and ops and ops[0] in ('*', '/'):
                op1 = ops.popleft()
                c = nums.popleft()
                if op1 == '*':
                    e = b * c
                else:
                    e = b // c
                nums.appendleft(e)
                nums.appendleft(a)
                ops.appendleft(op)
            else:
                if op == '+':
                    g = a + b
                elif op == '-':
                    g = a - b
                elif op == '*':
                    g = a * b
                else:
                    g = a // b
                nums.appendleft(g)

        return nums[0]


if __name__ == '__main__':
    print(Solution().calculate("3+2*2"))
    print(Solution().calculate(" 3/2 "))
    print(Solution().calculate(" 3+5 / 2 "))
    print(Solution().calculate('42'))
    print(Solution().calculate('0'))
    print(Solution().calculate('12-3*4'))
    print(Solution().calculate("1*2-3/4+5*6-7*8+9/10"))
    print(Solution().calculate("1+2*5/3+6/4*2"))

