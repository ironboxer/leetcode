"""
https://leetcode-cn.com/problems/3sum-closest/

16. 最接近的三数之和
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。



示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。


提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4

"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        s = 0
        diff = 1 << 8
        nums.sort()
        total = len(nums)
        for i in range(total - 2):
            n = nums[i]
            l, r = i + 1, total - 1
            while l < r:
                t = (n + nums[l] + nums[r])
                print(i, l, r)
                if abs(t - target) < diff:
                    s = t
                    diff = abs(t - target)
                if t < target:
                    l += 1
                elif t > target:
                    r -= 1
                else:
                    return s
        return s


if __name__ == '__main__':
    nums = [-1,2,1,-4]
    target = 1
    print(Solution().threeSumClosest(nums, target))

    nums = [0, 1, 2]
    target = 3
    print(Solution().threeSumClosest(nums, target))

