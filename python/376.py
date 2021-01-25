"""
https://leetcode.com/problems/wiggle-subsequence/


A sequence of numbers is called a wiggle sequence if the differences between successive numbers strictly alternate between positive and negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two elements is trivially a wiggle sequence.

For example, [1,7,4,9,2,5] is a wiggle sequence because the differences (6,-3,5,-7,3) are alternately positive and negative. In contrast, [1,4,7,2,5] and [1,7,4,5,5] are not wiggle sequences, the first because its first two differences are positive and the second because its last difference is zero.

Given a sequence of integers, return the length of the longest subsequence that is a wiggle sequence. A subsequence is obtained by deleting some number of elements (eventually, also zero) from the original sequence, leaving the remaining elements in their original order.

Example 1:

Input: [1,7,4,9,2,5]
Output: 6
Explanation: The entire sequence is a wiggle sequence.
Example 2:

Input: [1,17,5,10,13,15,10,5,16,8]
Output: 7
Explanation: There are several subsequences that achieve this length. One is [1,17,10,13,10,16,8].
Example 3:

Input: [1,2,3,4,5,6,7,8,9]
Output: 2
Follow up:
Can you do it in O(n) time?


Approach #2 Dynamic Programming
Algorithm

To understand this approach, take two arrays for dp named upup and downdown.

Whenever we pick up any element of the array to be a part of the wiggle subsequence, that element could be a part of a rising wiggle or a falling wiggle depending upon which element we have taken prior to it.

up[i]up[i] refers to the length of the longest wiggle subsequence obtained so far considering i^{th}i 
th
  element as the last element of the wiggle subsequence and ending with a rising wiggle.

Similarly, down[i]down[i] refers to the length of the longest wiggle subsequence obtained so far considering i^{th}i 
th
  element as the last element of the wiggle subsequence and ending with a falling wiggle.

up[i]up[i] will be updated every time we find a rising wiggle ending with the i^{th}i 
th
  element. Now, to find up[i]up[i], we need to consider the maximum out of all the previous wiggle subsequences ending with a falling wiggle i.e. down[j]down[j], for every j<i and nums[i]>nums[j]. Similarly, down[i]down[i] will be updated.

"""

from typing import List


class Solution0:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        def f(pos, flag):
            res = 0
            for i in range(pos + 1, len(nums)):
                if flag and nums[i] > nums[pos] or not flag and nums[i] < nums[pos]:
                    res = max(res, 1 + f(i, not flag))

            return res

        if len(nums) < 2:
            return len(nums)
        return 1 + max(f(0, True), f(0, False))


class Solution:
    """
    基本思路是什么?
    """
    def wiggleMaxLength(self, nums: List[int]) -> int:
        total = len(nums)
        if total < 2:
            return total
        up, down = [0] * total, [0] * total
        for i in range(1, total):
            for j in range(i):
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)

        return max(up[-1], down[-1]) + 1


if __name__ == '__main__':
    nums = [1,7,4,9,2,5]
    print(Solution().wiggleMaxLength(nums))

    nums = [1,17,5,10,13,15,10,5,16,8]
    print(Solution().wiggleMaxLength(nums))

    nums = [1,2,3,4,5,6,7,8,9]
    print(Solution().wiggleMaxLength(nums))

