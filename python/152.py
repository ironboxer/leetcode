"""
https://leetcode.com/problems/maximum-product-subarray/

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

"""

from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        A, B = [1] * (n + 1), [1] * (n + 1)
        for i, e in enumerate(nums):
            x = A[i] * e
            y = B[i] * e
            # 这个方法为什么是可行的?
            A[i + 1] = max(x, y, e)
            B[i + 1] = min(x, y, e)

        return max(A[1:])


# 这是一个很巧妙的思路, 两个数组就解决问题了, 根本用不到什么dp算法

if __name__ == '__main__':
    print(Solution().maxProduct([2, 3, -2, 4]))
    print(Solution().maxProduct([-2, 0, -1]))
    print(Solution().maxProduct([0, 2]))
