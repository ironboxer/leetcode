"""
https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/

剑指 Offer 21. 调整数组顺序使奇数位于偶数前面
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有奇数位于数组的前半部分，所有偶数位于数组的后半部分。



示例：

输入：nums = [1,2,3,4]
输出：[1,3,2,4]
注：[3,1,2,4] 也是正确的答案之一。


提示：

1 <= nums.length <= 50000
1 <= nums[i] <= 10000
"""

from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        A, B = [], []
        for n in nums:
            if n & 1:
                A.append(n)
            else:
                B.append(n)

        return A + B



class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1

        while l <= r:
            if nums[l] & 1:
                l += 1
            elif not nums[r] & 1:
                r -= 1
            else:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        return nums
