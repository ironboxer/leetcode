"""
https://leetcode.com/problems/next-greater-element-ii/

503. Next Greater Element II
Medium

1852

81

Add to List

Share
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        total = len(nums)
        nums += nums[:-1]
        res = [0] * (total * 2 - 1)
        stack = []
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            while stack and stack[-1] <= n:
                stack.pop()
            res[i] = stack[-1] if stack else -1
            stack.append(n)
        return res[:total]




# slow but work

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        total = len(nums)
        res = [-1] * total
        for i, e in enumerate(nums):
            for j in range(1,total):
                v = nums[(i + j) % total]
                if v > e:
                    res[i] = v
                    break

        return res


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        total = len(nums)
        res = [-1] * total
        stack = []
        for i in range(2 * total - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % total]:
                stack.pop()
            res[i % total] = nums[stack[-1]] if stack else -1
            stack.append(i % total)

        return res


if __name__ == '__main__':
    nums = [1,2,1]
    print(Solution().nextGreaterElements(nums))

