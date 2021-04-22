"""
https://leetcode.com/problems/3sum

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums)-1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s > 0:
                    right -= 1
                elif s < 0:
                    left += 1
                else:
                    buf = [nums[i], nums[left], nums[right]]
                    res.append(buf)
                    left, right = left + 1, right - 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return res



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        def f(nums, target):
            res = []
            left, right = 0, len(nums) - 1
            while left < right:
                s = nums[left] + nums[right]
                if s < target:
                    left += 1
                elif s > target:
                    right -= 1
                else:
                    res.append([nums[left], nums[right]])
                    left, right = left + 1, right - 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            return res

        nums.sort()
        res = []
        for i, e in enumerate(nums):
            if i > 0 and e == nums[i-1]:
                continue
            buf = f(nums[i+1:], 0 - e)
            if buf:
                res += [[e] + items for items in buf]

        return res



# 费了很大的力气 每次做题的时候都感觉力不从心啊
class Solution:

    @staticmethod
    def find_two(nums, l, r, target):
        retval = []

        while l < r:
            val = nums[l] + nums[r]
            if val < target:
                l += 1
            elif val > target:
                r -= 1
            else:
                retval.append([nums[l], nums[r]])
                l, r = l + 1, r - 1
                while l < r and nums[l] == nums[l-1]:
                    l += 1
                while l < r and nums[r] == nums[r+1]:
                    r -= 1

        return retval

    def nth(self, nums, l, r, n, target):
        if n == 2:
            return self.find_two(nums, l, r, target)

        retval = []
        for i in range(l, r + 1):
            # unique
            if i > 0 and nums[i] == nums[i-1]:
                continue
            arr = self.nth(nums, i + 1, r, n - 1, target - nums[i])
            retval += [[nums[i]] + items for items in arr]

        return retval

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        return self.nth(nums, 0, len(nums) - 1, 3, 0)




class Solution:

    @staticmethod
    def twoSum(nums, low, high, target):
        res = []
        while low < high:
            val = nums[low] + nums[high]
            if val < target:
                low += 1
            elif val > target:
                high -= 1
            else:
                res.append([nums[low], nums[high]])
                low, high = low + 1, high - 1
                while low < high and nums[low] == nums[low-1]:
                    low += 1
                while low < high and nums[high] == nums[high + 1]:
                    high -= 1
        return res


    @classmethod
    def nthSum(cls, nums, low, high, target, n):
        if n == 2:
            return cls.twoSum(nums, low, high, target)
        res = []
        for i in range(low, high):
            val = nums[i]
            if i > low and val == nums[i-1]:
                continue
            buf = cls.nthSum(nums, i+1, high, target - val, n - 1)
            res += [[val] + items for items in buf]
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.nthSum(nums, 0, len(nums) - 1, 0, 3)


# 整个思路非常清晰
# 因为问题并不难理解 如果是动态规划 需要把整个问题空间和解空间都想明白了 
# 心智负担非常的大


if __name__ == "__main__":
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([3, 0, -2, -1, 1, 2]))
    print(Solution().threeSum([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]))
