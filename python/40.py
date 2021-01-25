"""
https://leetcode.com/problems/combination-sum-ii/

Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]

0-1 背包 不放回
"""

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()

        def f(start, buf, t):
            # print(nums, t)
            if t == 0:
                res.add(tuple(buf[:]))
                return
            for i in range(start, len(candidates)):
                n = candidates[i]
                if n > t:
                    break
                if buf and buf[-1] > n:
                    continue
                buf.append(n)
                f(i+1, buf, t - n)
                buf.pop()

        f(0, [], target)
        return [list(i) for i in res]

class Solution2:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def f(start, buf, t):
            if t == 0:
                res.append(buf[:])
                return
            for i in range(start, len(candidates)):
                if i > start and candidates[i] > candidates[i-1]:
                    continue
                e = candidates[i]
                if e > t:
                    break
                if buf and buf[-1] > e:
                    continue
                buf.append(e)
                f(i+1, buf, t - e)
                buf.pop()

        f(0, [], target)
        return res


class Solution3:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def f(start, buf, t):
            if t == 0:
                res.append(buf[:])
                return
            for i in range(start, len(candidates)):
                e = candidates[i]
                if e > t:
                    break
                # 需要好好想一下才能清楚为什么要在这个地方加一个判断
                # 是为了防止一个新的rouine从重复的元素开始, 因为这样就重复了
                # 比如 nums = [2,2,2,3]
                if i > start and e == candidates[i-1]:
                    continue
                if buf and buf[-1] > e:
                    continue
                buf.append(e)
                f(i+1, buf, t - e)
                buf.pop()

        f(0, [], target)
        return res


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def f(pos, target, buf):
            if target == 0:
               res.append(buf[:])
               return
            for i in range(pos, len(candidates)):
                e = candidates[i]
                if i > pos and e == candidates[i-1]:
                    continue
                if e > target:
                    break
                buf.append(e)
                f(i+1, target - e, buf)
                buf.pop()

        f(0, target, [])

        return res


#  做一万遍都不会啊


if __name__ == "__main__":
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    print(Solution2().combinationSum2(candidates, target))
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(Solution2().combinationSum2(candidates, target))
