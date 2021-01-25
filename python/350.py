"""
https://leetcode.com/problems/intersection-of-two-arrays-ii/

Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?

"""


from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        from collections import Counter
        a, b = Counter(nums1), Counter(nums2)
        c, d = set(a), set(b)
        s = c.intersection(d)
        res = []
        for i in s:
            t = min(a[i], b[i])
            p = [i] * t
            res.extend(p)
        return res

if __name__ == '__main__':
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(Solution().intersect(nums1, nums2))

    nums1 = [1,2,2,1]
    nums2 = [2,2]
    print(Solution().intersect(nums1, nums2))

