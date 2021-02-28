"""
https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

剑指 Offer 11. 旋转数组的最小数字
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。

示例 1：

输入：[3,4,5,1,2]
输出：1
示例 2：

输入：[2,2,2,0,1]
输出：0
注意：本题与主站 154 题相同：https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""

from typing import List


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l, r = 0, len(numbers) - 1
        while l <= r:
            m = (l + r) >> 1
            # numbers[r] < numbers[m] => 最小值在右侧
            if numbers[r] < numbers[m]:
                l = m + 1
            #  numbers[r] >= numbers[m] => numbers[r]不是最小值 排除掉
            else:
                r -= 1
        # print(l, r)
        return numbers[l]


# SLOW BUT WORK
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        # 核心还是根据二分查找的基本原则
        # 在符合递增的区间中 尽量的做排除
        # 能够进行二分查找的 就用二分查找
        # 无法使用二分查找的 只能够使用遍历的方式
        l, r = 0, len(numbers) - 1
        while l < r:
            mid = (l + r) // 2
            if numbers[mid] > numbers[r]:
                l = mid + 1
            elif numbers[mid] < numbers[l]:
                r = mid
            else:
                r -= 1

        return numbers[r]


if __name__ == '__main__':

    nums = [2,2,2,0,1]
    print(Solution().minArray(nums))

    nums = [3,4,5,1,2]
    print(Solution().minArray(nums))

