"""
https://leetcode.com/problems/wiggle-sort-ii/

Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2] < nums[3]....

Example 1:

Input: nums = [1, 5, 1, 1, 6, 4]
Output: One possible answer is [1, 4, 1, 5, 1, 6].
Example 2:

Input: nums = [1, 3, 2, 2, 3, 1]
Output: One possible answer is [2, 3, 1, 3, 1, 2].
Note:
You may assume all input has valid answer.

Follow Up:
Can you do it in O(n) time and/or in-place with O(1) extra space?

"""


from typing import List


class Solution:
    """
    注意 i和j的位置
    """
    def wiggleSort(self, nums: List[int]) -> None:
        arr = sorted(nums)
        total = len(nums)
        mid = (total + 1) // 2
        i, j = mid - 1, total - 1
        for k in range(total):
            if k & 1:
                nums[k] = arr[j]
                j -= 1
            else:
                nums[k] = arr[i]
                i -= 1


if __name__  == '__main__':
    nums = [1, 5, 1, 1, 6, 4]
    print(nums)
    Solution().wiggleSort(nums)
    print(nums)

    nums = [1, 3, 2, 2, 3, 1]
    print(nums)
    Solution().wiggleSort(nums)
    print(nums)

