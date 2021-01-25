"""
https://leetcode.com/problems/first-missing-positive

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Follow up:

Your algorithm should run in O(n) time and uses constant extra space.

"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            # TODO: 以当前的元素为准, 而不是当前的下标
            while 0 < nums[i] <= N and nums[nums[i] - 1] != nums[i]:
                # 在替换的时候需要小心一下, 这个是Python的锅
                e = nums[i]
                nums[i], nums[e - 1] = nums[e - 1], nums[i]

        for i in range(N):
            if nums[i] != i + 1:
                return i + 1

        return N + 1


if __name__ == "__main__":
    cases = [
        [[1, 2, 0], 3],
        [[3, 4, -1, 1], 2],
        [[7, 8, 9, 11, 12], 1],
    ]
    for nums, res in cases:
        r = Solution().firstMissingPositive(nums)
        print(nums, res, r)
        assert res == r
