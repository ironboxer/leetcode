"""
https://leetcode.com/problems/top-k-frequent-elements/

Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
It's guaranteed that the answer is unique, in other words the set of the top k frequent elements is unique.
You can return the answer in any order.

"""


from typing import List


class Solution0:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        return [i for i, _  in Counter(nums).most_common(k)]


class Solution1:
    """
    无法解决元素的频次重复的问题
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) + 1
        m = {v: k for k, v in d.items()}
        r = [-v for v in m]

        from heapq import heappop, heapify
        heapify(r)
        v = [-heappop(r) for _ in range(k)]
        return [m[i] for i in v]


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter, defaultdict
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        for key, val in freq.items():
            bucket[val].append(key)
        res = []
        for p in range(len(bucket) - 1, -1, -1):
            if bucket[p]:
                res.extend(bucket[p])
                if len(res) >= k:
                    break
        return res[:k]


if __name__ == '__main__':
    nums = [1,1,1,2,2,3]
    k = 2
    print(Solution().topKFrequent(nums, k))


    nums = [10, 10, 10, 10, 10]
    k = 2
    print(Solution().topKFrequent(nums, k))

