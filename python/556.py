"""
https://leetcode.com/problems/next-greater-element-iii/

556. Next Greater Element III
Medium

790

215

Add to List

Share
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:

Input: 12
Output: 21


Example 2:

Input: 21
Output: -1
"""


# 这是个啥题呢?


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        pass


# Slow but work

from itertools import permutations


class Solution:
    def nextGreaterElement(self, n: int) -> int:
        for item in sorted(permutations(str(n))):
            x = int(''.join(item))
            if x > n:
                return x if x < (1 << 31) else -1
        return -1


class Solution:
    """
    这道题很难说出什么东西 但是可以用举例的方式来说明
    比如 12345 54321 12435
    通过分别代入这几个例子 就知道算法的解题思路了

    """
    def nextGreaterElement(self, n: int) -> int:
        nums = list(map(int, str(n)))
        stack = [nums.pop()]
        while nums and stack[-1] <= nums[-1]:
            stack.append(nums.pop())
        if not nums:
            return -1
        for j in range(len(stack)):
            if stack[j] > nums[-1]:
                stack[j], nums[-1] = nums[-1], stack[j]
                break

        retval = int(''.join(map(str, nums + stack)))
        return retval if retval < 1 << 31 else -1


if __name__ == '__main__':
    pass


