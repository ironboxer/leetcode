"""
https://leetcode.com/problems/merge-sorted-array/
"""
from typing import List


class Solution1:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, p = m - 1, n - 1, len(nums1) - 1
        while j >= 0:
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i, j, p = m - 1, n - 1, m + n - 1
        while i >= 0 and j >= 0:
            if nums1[i] >= nums2[j]:
                nums1[p] = nums1[i]
                i -= 1
            else:
                nums1[p] = nums2[j]
                j -= 1
            p -= 1
        # i == 0并不意味着迭代的终止, 只表明 nums1的元素都遍历完了
        # 但是 nums2中的元素不一定遍历完了, nums[p] 还有空间给nums2放置元素呢
        while j >= 0:
            nums1[p] = nums2[j]
            j -= 1
            p -= 1


if __name__ == '__main__':
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    Solution().merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    print(nums1)

    nums1 = [2, 0]
    m = 1
    nums2 = [1]
    n = 1
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
