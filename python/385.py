"""
https://leetcode.com/problems/mini-parser/

Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:

String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].


Example 1:

Given s = "324",

You should return a NestedInteger object which contains a single integer 324.


Example 2:

Given s = "[123,[456,[789]]]",

Return a NestedInteger object containing a nested list with 2 elements:

1. An integer containing value 123.
2. A nested list containing two elements:
    i.  An integer containing value 456.
    ii. A nested list with one element:
         a. An integer containing value 789.

"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution0:
    def deserialize(self, s: str):
        import json
        nums = json.loads(s)

        def f(arr):
            if isinstance(arr, int):
                return NestedInteger(arr)
            else:
                i = NestedInteger()
                for item in arr:
                    i.add(f(item))
                return i

        return f(nums)


class Solution:
    def deserialize(self, s: str):

        def f(e):
            if isinstance(e, int):
                return NestedInteger(e)
            i = NestedInteger()
            for j in e:
                i.add(f(j))
            return i

        # 这段代码中有补丁的
        # stack2 就是一个典型的补丁
        # 实际上有更好的方法
        def p(s):
            stack = []
            stack2 = []
            num = ''
            cur = stack
            for c in s:
                if c == ',':
                    if num:
                        cur.append(int(num))
                        num = ''
                elif c == '[':
                    stack2.append(cur)
                    new_cur = []
                    cur.append(new_cur)
                    cur = new_cur
                elif c == ']':
                    if num:
                        cur.append(int(num))
                        num = ''
                    cur = stack2.pop()
                else:
                    num += c
            if num:
                stack.append(int(num))

            return stack[0] if stack else stack

        buf = p(s)
        print(buf)
        return f(buf)


# 这是最为简单的LL Parser


# why this worked?
class Solution:
    def deserialize(self, s):
        stack, num, last = [], "", None
        for c in s:
            # number
            if c.isdigit() or c == '-':
                num += c
            # for current number
            elif c == ',' and num:
                stack[-1].add(NestedInteger(int(num)))
                num = ''
            elif c == '[':
                elem = NestedInteger()
                if stack:
                    stack[-1].add(elem)
                stack.append(elem)
            elif c == ']':
                if num:
                    stack[-1].add(NestedIneteger(int(num)))
                    num = ''
                last = stack.pop()

        return last if last else NestedInteger(int(num))



class Solution:
    def deserialize(self, s):
        digits = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-'}

        def f():
            num = ''
            while s[-1] in digits:
                num += s.pop()
            if num:
                return NestedInteger(int(num))
            s.pop()
            lst = NestedInteger()
            while s[-1] != ']':
                lst.add(NestedInteger())
                if s[-1] != ']':
                    s.pop()
            s.pop()
            return lst

        # why reverse the string?
        s = list(' ' + s[::-1])

        return f()


# QUESTION: how to tokenize it ?
def tokenize(s):
    tokens = []
    num = ''
    for c in s:
        if c == '[':
            tokens.append(c)
        elif c.isdigit() or c == '-':
            num += c
        elif c == ',':
            if num:
                tokens.append(int(num))
                num = ''
            tokens.append(c)
        elif c == ']':
            if num:
                tokens.append(int(num))
                num = ''
            tokens.append(c)
    if num:
        tokens.append(int(num))
        num = ''

    return tokens


# 恰好蒙中了
def decode(tokens):
    # ['[', 123, ',', '[', 456, ',', '[', 789, ']', ']', ']']
    #print(tokens)
    stack = [[]]
    item = None
    for token in tokens:
        if token == "[":
            stack.append([])
        elif token == ",":
            top = stack.pop()
            if item is not None:
                top.append(item)
                item = None
            stack.append(top)
        elif token == "]":
            top = stack.pop()
            if item is not None:
                top.append(item)
                item = None
            stack[-1].append(top)
        else:
            item = token

    if item is not None:
        top = stack.pop()
        top.append(item)
        item = None
        stack.append(top)

    top = stack.pop()
    return top.pop() if top else top


if __name__ == '__main__':
    s = "-3"
    tks = tokenize(s)
    print(decode(tks))

    s = "324"
    tks = tokenize(s)
    print(decode(tks))

    s = "[123,[456,[789]]]"
    tks = tokenize(s)
    print(decode(tks))

    s = "[123]"
    tks = tokenize(s)
    print(decode(tks))

    s =  "[]"
    tks = tokenize(s)
    print(decode(tks))

    s = "[123,456,[788,799,833],[[]],10,[]]"
    print(s)
    tks = tokenize(s)
    print(decode(tks))


class Solution:

    def deserialize(self, s):

        def f(arr):
            if isinstance(arr, int):
                return NestedInteger(arr)
            else:
                i = NestedInteger()
                for item in arr:
                    i.add(f(item))
                return i

        tokens = tokenize(s)
        lst = decode(tokens)
        return f(lst)


if __name__ == '__main__1':
    s = "324"
    print(Solution().deserialize(s))

    s = "[123,[456,[789]]]"
    print(Solution().deserialize(s))

