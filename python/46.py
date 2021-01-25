"""
https://leetcode.com/problems/permutations/

Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def f(pos):
            if pos == len(nums):
                res.append(nums[:])
                return

            for i in range(pos, len(nums)):
                nums[i], nums[pos] = nums[pos], nums[i]
                f(pos + 1)
                nums[i], nums[pos] = nums[pos], nums[i]

        f(0)
        return res


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().permute(nums))
