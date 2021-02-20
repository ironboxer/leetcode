"""
https://leetcode.com/problems/subarray-sum-equals-k/

560. Subarray Sum Equals K
Medium

5821

193

Add to List

Share
Given an array of integers nums and an integer k, return the total number of continuous subarrays whose sum equals to k.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2


Constraints:

1 <= nums.length <= 2 * 104
-1000 <= nums[i] <= 1000
-107 <= k <= 107
"""



from typing import List


# 备忘录模式
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = {0: 1}
        res = 0
        i = 0
        for n in nums:
            i += n
            j = i - k
            res += prefix.get(j, 0)
            prefix[i] = prefix.get(i, 0) + 1
        return res


# SLOW BUT WORK
# TLE
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        for i in range(len(nums)):
            s = 0
            for j in range(i, len(nums)):
                s += nums[j]
                if s == k:
                    res += 1
        return res


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        retval = 0
        prev_sum, cur_sum = 0, 0
        # 表示prev_sum == cur_sum
        sum_table = {0: 1}
        for n in nums:
            cur_sum += n
            prev_sum = cur_sum - k
            retval += sum_table.get(prev_sum, 0)
            sum_table[cur_sum] = sum_table.get(cur_sum, 0) + 1

        return retval


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    print(Solution().subarraySum(nums, k))

    nums = [1,2,3]
    k = 3
    print(Solution().subarraySum(nums, k))

    nums = [1,2,1,2,1]
    k = 3
    print(Solution().subarraySum(nums, k))

