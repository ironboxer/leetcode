"""
https://leetcode-cn.com/problems/squares-of-a-sorted-array/

977. 有序数组的平方
给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。



示例 1：

输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]
示例 2：

输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]


提示：

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
"""


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i, total = 0, len(nums)
        C = [0] * total
        while i < total:
            n = nums[i]
            if n >= 0:
                break
            i += 1

        l, r, k = i - 1, i, 0
        while l >= 0 and r < total:
            a, b = nums[l] ** 2, nums[r] ** 2
            if a <= b:
                C[k] = a
                l -= 1
            else:
                C[k] = b
                r += 1
            k += 1

        while l >= 0:
            C[k] = nums[l] ** 2
            k += 1
            l -= 1

        while r < total:
            C[k] = nums[r] ** 2
            k += 1
            r += 1

        return C
