"""
https://leetcode.com/problems/combination-sum

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]

class Solution(object):
def combinationSum(self, candidates, target):
    result = []
    candidates = sorted(candidates)
    def dfs(remain, stack):
        if remain == 0:
            result.append(stack)
            return 

        for item in candidates:
            if item > remain: break
            if stack and item < stack[-1]: continue
            else:
                dfs(remain - item, stack + [item])
    
    dfs(target, [])
    return result
"""

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = set()

        def f(buf, t):
            # print(buf, t)
            if t == 0:
                res.add(tuple(sorted(buf[:])))
                return
            for c in candidates:
                if c > t:
                    break
                tmp = buf[:]
                tmp.append(c)
                f(tmp, t - c)
                # f(buf, t)

        f([], target)
        return [list(i) for i in res]

# 0 - 1 背包

class Solution2:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = set()
        
        def f(buf, t):
            if t == 0:
                res.add(tuple(sorted(buf[:])))
                return
            for c in candidates:
                if c > t:
                    break
                buf.append(c)
                f(buf[:], t - c)
                buf.pop()

        f([], target)
        return [list(i) for i in res]



class Solution3:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def f(buf, t):
            if t == 0:
                res.append(buf[:])
                return
            for c in candidates:
                if c > t:
                    break
                if buf and c < buf[-1]:
                    print("hit", buf, c, t)
                    continue
                buf.append(c)
                f(buf[:], t - c)
                buf.pop()

        f([], target)
        return res


class Solution4:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        
        def f(buf, t):
            if t == 0:
                res.append(buf[:])
                return

            for c in candidates:
                if c > t:
                    break
                if buf and c < buf[-1]:
                    # print("hit", buf, c, t)
                    continue
                buf.append(c)
                f(buf, t - c)
                buf.pop()

        f([], target)
        return res


if __name__ == "__main__":
    cases = [
        ([2, 3, 6, 7], 7),
        ([2, 3, 5], 8),
    ]
    for candidates, target in cases:
        print(Solution4().combinationSum(candidates, target))
