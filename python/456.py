"""
https://leetcode-cn.com/problems/132-pattern/


456. 132模式
给定一个整数序列：a1, a2, ..., an，一个132模式的子序列 ai, aj, ak 被定义为：当 i < j < k 时，ai < ak < aj。设计一个算法，当给定有 n 个数字的序列时，验证这个序列中是否含有132模式的子序列。

注意：n 的值小于15000。

示例1:

输入: [1, 2, 3, 4]

输出: False

解释: 序列中不存在132模式的子序列。
示例 2:

输入: [3, 1, 4, 2]

输出: True

解释: 序列中有 1 个132模式的子序列： [1, 4, 2].
示例 3:

输入: [-1, 3, 2, 0]

输出: True

解释: 序列中有 3 个132模式的的子序列: [-1, 3, 2], [-1, 3, 0] 和 [-1, 2, 0].
"""


from typing import List

from itertools import combinations


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        for a, b, c in combinations(nums, 3):
            if a < c < b:
                return True
        return False



class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        A = [0] * len(nums)
        for i, e in enumerate(nums):
            if i == 0:
                A[i] = e
            else:
                A[i] = min(e, A[i-1])
        print(A)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            if n > A[i]:
                while stack and stack[-1] <= A[i]:
                    stack.pop()
                if stack and stack[-1] < n:
                    return True
                stack.append(n)
        return False


# SLOW BUT WORK
# TLE
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        for i in range(0, len(nums)-2):
            for j in range(i+1, len(nums)-1):
                for k in range(j+1, len(nums)):
                    if nums[i] < nums[k] < nums[j]:
                        return True
        return False


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        total = len(nums)
        if total < 2:
            return False
        mi = [nums[0]]
        for i in range(1, total):
            mi.append(min(nums[i], mi[-1]))

        stack = []
        for i in range(total - 1, -1, -1):
            if nums[i] > mi[i]:
                while stack and mi[i] >= stack[-1]:
                    stack.pop()
                # 说明 stack[-1] > mi[i]
                # 否则stack就被pop空了
                if stack and stack[-1] < nums[i]:
                    return True
                # 加入当前的元素
                stack.append(nums[i])

        return False


if __name__ == '__main__':
    nums = [2,3,1,2]
    print(nums)
    print(Solution().find132pattern(nums))


