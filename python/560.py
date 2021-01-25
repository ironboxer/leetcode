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

