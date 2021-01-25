"""
https://leetcode.com/problems/jump-game/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

 

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 3 * 10^4
0 <= nums[i][j] <= 10^5

"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        i, nxt = 0, nums[0]
        while i < N and i <= nxt:
            nxt = max(nxt, i + nums[i])
            i += 1
        return nxt >= len(nums) - 1

# 最后还是过了, 还是那些事, 需要稍微简单的想一想

if __name__ == '__main__':
    cases = [
        ([1, 2, 3], True),
        ([0, 2, 3], False),
        ([2, 3, 1, 1, 4], True),
        ([3, 2, 1, 0, 4], False),
    ]
    for nums, ret in cases:
        r = Solution().canJump(nums)
        print(nums, ret, r)
        assert ret == r
