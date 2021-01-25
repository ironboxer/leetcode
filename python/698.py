"""
https://leetcode-cn.com/problems/partition-to-k-equal-sum-subsets/


698. 划分为k个相等的子集
给定一个整数数组  nums 和一个正整数 k，找出是否有可能把这个数组分成 k 个非空子集，其总和都相等。

示例 1：

输入： nums = [4, 3, 2, 3, 5, 2, 1], k = 4
输出： True
说明： 有可能将其分成 4 个子集（5），（1,4），（2,3），（2,3）等于总和。


提示：

1 <= k <= len(nums) <= 16
0 < nums[i] < 10000

"""

from typing import List

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        target, rem = divmod(sum(nums), k)
        if rem:
            return False

        def search(groups):
            if not nums:
                return True

            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if search(groups):
                        return True
                    groups[i] -= v
                if not group:
                    break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target:
            return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1

        return search([0] * k)


if __name__ == '__main__':
    nums = [2,2,2,2,3,4,5]
    k = 4
    print(Solution().canPartitionKSubsets(nums, k))

    nums = [10,10,10,7,7,7,7,7,7,6,6,6]
    k = 3
    print(Solution().canPartitionKSubsets(nums, k))

