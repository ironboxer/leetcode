"""
https://leetcode.com/problems/contains-duplicate/

Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true

Example 2:

Input: [1,2,3,4]
Output: false

Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List

# why?
# 你看懂了吗
# 原理是什么呢？
# 抄了一遍代码 但是什么都不清楚
# 说明这就是智商税啊
# 因为你根本不清楚这其中的原因是什么
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        pos = 0
        neg = 0
        for n in nums:
            mask = 1 << abs(n)
            if n >= 0:
                if pos & mask:
                    return True
                else:
                    pos ^= mask
            else:
                if neg & mask:
                    return True
                else:
                    neg ^= mask
            print(pos, neg)
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))


if __name__ == '__main__':
    print(Solution().containsDuplicate([1,2,3,1]))
    print(Solution().containsDuplicate([1,2,3,4]))
    print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    print(Solution().containsDuplicate([-1200000005,-1200000005]))

