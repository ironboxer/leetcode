"""
https://leetcode-cn.com/problems/maximum-swap/

670. 最大交换
给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。
注意:

给定数字的范围是 [0, 108]

"""



class Solution:
    def maximumSwap(self, num: int) -> int:

        def cal(nums):
            r = 0
            for n in nums:
                r = r * 10 + n
            return r

        nums = []
        while num:
            nums.append(num %10)
            num //= 10

        pos = {}
        nums = nums[::-1]
        nums_sort = sorted(nums, reverse=True)

        for i, e in enumerate(nums):
            if e not in pos:
                pos[e] = []
            pos[e].append(i)

        for i, e in enumerate(nums):
            if e != nums_sort[i]:
                j = pos[nums_sort[i]][-1]
                nums[i], nums[j] = nums[j], nums[i]
                break

        return cal(nums)

