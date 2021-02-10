"""
https://leetcode.com/problems/range-sum-query-mutable/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.
Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8


Constraints:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
0 <= i <= j <= nums.length - 1

http://codeforces.com/blog/entry/18051

---
n = 10
nums = [1,2,3,4,5,6,7,8,9,10]
prefix = [0,1,3,6,10,15,21,28,36,45,55]

当更新nums[i]的时候, prefix[i] -> prefix[n]之间的元素都需要更新, 显然时间复杂度为O(n)
segment tree 的好处就是 可以将时间复杂度减小到O(log(n))

segment tree 的prefix数组中存储的并不是 prefix[j] = sum(num[1] -> nums[j])
而是一个二进制的路径 这个路径的最大长度不大于n的二进制的位数
"""


from typing import List

# 线段树
class SegmentTree:
    def __init__(self, n):
        self._sums = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self._sums):
            self._sums[i] += delta
            i += i & -i

    def query(self, i):
        s = 0
        while i > 0:
            s += self._sums[i]
            i -= i & -i
        return s


class NumArray:

    def __init__(self, nums: List[int]):
        self._nums = nums
        self._tree = SegmentTree(len(nums))
        for i in range(len(nums)):
            self._tree.update(i+1, nums[i])

    def update(self, i: int, val: int) -> None:
        self._tree.update(i + 1, val - self._nums[i])
        self._nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return self._tree.query(j + 1) - self._tree.query(i)


if __name__ == '__main__':
    nums = [1, 3, 5]
    print(nums)
    s = NumArray(nums)
    print(s._tree._sums)
    print(s.sumRange(0, 2))

    s.update(1, 2)
    print(s._tree._sums)
    print(s.sumRange(0, 2))

    s.update(1, 11)
    print(s._tree._sums)
    print(s.sumRange(0, 2))

