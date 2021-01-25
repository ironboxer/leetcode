"""
https://leetcode.com/problems/next-permutation

Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1


https://leetcode.com/problems/next-permutation/discuss/13867/C%2B%2B-from-Wikipedia

1. Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
2. Find the largest index l > k such that nums[k] < nums[l].
3. Swap nums[k] and nums[l].
4. Reverse the sub-array nums[k + 1:].
"""

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        k = N - 2
        while k >= 0:
            if nums[k] < nums[k+1]:
                break
            k -= 1
        if k < 0:
            nums[:] = nums[::-1]
        else:
            for l in range(N-1, k, -1):
                if nums[l] > nums[k]:
                    break
            nums[k], nums[l] = nums[l], nums[k]
            nums[k+1:] = nums[k+1:][::-1]

# 这段普通的代码 很有玄机
# 可以带入几种情况试一下, 很准确

if __name__ == "__main__":
    # nums = [1, 2, 3]
    nums = [3, 2, 1]
    Solution().nextPermutation(nums)
    print(nums)
