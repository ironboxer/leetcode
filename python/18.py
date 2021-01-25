"""

https://leetcode.com/problems/4sum/

Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

"""
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        from collections import Counter
        dic = Counter(nums)
        res = set()
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                a, b = nums[i], nums[j]
                for k in range(j+1, N):
                    c = nums[k]
                    d = target - a - b - c
                    cnt = dic[d]
                    if cnt > 0:
                        buf = [a, b, c, d]
                        for e in buf:
                            dic[e] -= 1
                        for e in buf:
                            if dic[e] < 0:
                                break
                        else:
                            res.add(tuple(sorted([a, b, c, d])))
                        for e in buf:
                            dic[e] += 1
        return [list(item) for item in res]


# a new solution
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return
        if N == 2:
            l, r = 0, len(nums) - 1
            while l < r:
                print(l, r, nums[l], nums[r], target)
                if nums[l] + nums[r] == target:
                    print("hit")
                    results.append(result + [nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    r -= 1
        else:
            for i in range(0, len(nums) - N + 1):
                if target < nums[i] * N or target > nums[-1] * N:
                    break
                if i == 0 or i > 0 and nums[i-1] != nums[i]:
                    self.findNsum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)



class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i, e in enumerate(nums):
            if i > 0 and e == nums[i-1]:
                continue
            items = self.threeSum(nums[i+1:], target - e)
            if items:
                res += [[e] + item for item in items]

        return res


    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:

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

        res = []
        for i, e in enumerate(nums):
            if i > 0 and e == nums[i-1]:
                continue
            buf = f(nums[i+1:], target - e)
            if buf:
                res += [[e] + items for items in buf]

        return res



class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = self.nSum(nums, target, 4)
        return res

    @staticmethod
    def nSum(nums: List[int], target: int, n: int) -> List[List[int]]:
        if n == 2:
            return Solution.twoSum(nums, target)
        res = []
        for i, e in enumerate(nums):
            if i > 0 and e == nums[i-1]:
                continue
            items = Solution().nSum(nums[i+1:], target - e, n - 1)
            if items:
                res += [[e] + item for item in items]

        return res

    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[List[int]]:
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


# 题做多了 就是有模板



def twoSum(nums, target):
    res = []
    l, r = 0, len(nums) - 1
    while l < r:
        a, b = nums[l], nums[r]
        s = a + b
        if s < target:
            l += 1
        elif s > target:
            r -= 1
        else:
            res.append([a, b])
            l, r = l + 1, r - 1
            while l < r and nums[l] == a:
                l += 1
            while l < r and nums[r] == b:
                r -= 1
    return res


def nSum(nums, n, target):
    if n == 2:
        return twoSum(nums, target)
    res = []
    total = len(nums)
    for i in range(total - n + 1):
        e = nums[i]
        if i > 0 and e == nums[i-1]:
            continue
        buf = nSum(nums[i+1:], n-1, target - nums[i])
        res.extend([e] + items for items in buf)
    return res


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return nSum(nums, 4, target)



if __name__ == "__main__":
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))

