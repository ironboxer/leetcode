"""
https://leetcode.com/problems/jump-game-ii

Given an array of non-negative integers, you are initially positioned at the first index of the   array.
 
Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.

"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        lastpos, maxpos, step = 0, 0, 0
        for i, e in enumerate(nums):
            if i > lastpos:
                lastpos = maxpos
                step += 1
            maxpos = max(maxpos, i + e)
        return step


if __name__ == "__main__":
    nums = [2, 3, 1, 1, 4]
    print(Solution().jump(nums))
    nums = [0]
    print(Solution().jump(nums))
    nums = [2, 0, 2, 0, 1]
    print(Solution().jump(nums))
