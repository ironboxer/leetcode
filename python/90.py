"""
https://leetcode.com/problems/subsets-ii/

Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

from typing import List


class Solution1:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res.extend([[n] + i for i in res])
        return list((list(j) for j in set(tuple(sorted(i)) for i in res)))


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def f(buf, pos):
            res.append(buf[:])
            for i in range(pos, len(nums)):
                # 在有连续重复元素的情况下, 跳过
                if i > pos and nums[i] == nums[i-1]:
                    continue
                buf.append(nums[i])
                f(buf, i + 1)
                buf.pop()

        f([], 0)
        return res


if __name__ == '__main__':
    nums = [1, 2, 2]
    print(Solution().subsetsWithDup(nums))
