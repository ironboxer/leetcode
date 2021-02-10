"""
https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/

315. 计算右侧小于当前元素的个数
给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于 nums[i] 的元素的数量。



示例：

输入：nums = [5,2,6,1]
输出：[2,1,1,0]
解释：
5 的右侧有 2 个更小的元素 (2 和 1)
2 的右侧仅有 1 个更小的元素 (1)
6 的右侧有 1 个更小的元素 (1)
1 的右侧有 0 个更小的元素


提示：

0 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

"""

from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    res[i] += 1
        return res



from bisect import bisect_left

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        window = []
        for i in range(len(nums) - 1, -1, -1):
            n = nums[i]
            j = bisect_left(window, n)
            res[i] = j
            # 这个地方需要移动元素 效率比较低
            # 最坏情况下为O(n^2)
            window.insert(j, n)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        size = len(nums)
        if size == 0:
            return []
        if size == 1:
            return [0]
        arr = [(i, e) for i, e in enumerate(nums)]
        self.res = [0] * size
        self.merge_sort(arr, 0, size-1)
        return self.res

    def merge_sort(self, nums, left, right):
        if left >= right:
            return
        mid = (left + right) // 2
        self.merge_sort(nums, left, mid)
        self.merge_sort(nums, mid+1, right)

        # short circurt
        # 最侧的最大元素小于右侧的最小元素 不需要合并了 已经是有序的
        if nums[mid][1] <= nums[mid+1][1]:
            return

        self.merge(nums, left, mid, right)

    def merge(self, nums, left, mid, right):
        i, j, k = left, mid+1, 0
        buf = [0] * (right - left + 1)
        while i <= mid and j <= right:
            if nums[i][1] <= nums[j][1]:
                self.res[nums[i][0]] += j - mid - 1
                buf[k] = nums[i]
                i += 1
            else:
                buf[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            self.res[nums[i][0]] += j - mid - 1
            buf[k] = nums[i]
            k += 1
            i += 1

        while j <= right:
            buf[k] = nums[j]
            k += 1
            j += 1

        for p in range(k):
            nums[left + p] = buf[p]



def merge_sort(nums, low, high, counts):
    if low >= high:
        return

    mid = (low + high) // 2
    merge_sort(nums, low, mid, counts)
    merge_sort(nums, mid+1, high, counts)

    # merge
    C = [0] * (high - low + 1)
    i, j, k = low, mid+1, 0
    while i <= mid and j <= high:
        if nums[i][1] <= nums[j][1]:
            # 这里之所以没有想到用这种方式
            # 就是因为没有搞清楚这里的数据结构是如何设计的
            # 搞明白了数据结构 后面的就好理解了
            # 归并排序使得左侧的元素L与右侧的元素R可以一一比较
            # 如果没有比较到 说明当前的元素E是最小的 右侧不可能有比他还小的元素了
            counts[nums[i][0]] += j - mid - 1
            C[k] = nums[i]
            i += 1
        else:
            C[k] = nums[j]
            j += 1
        k += 1

    while i <= mid:
        counts[nums[i][0]] += j - mid - 1
        C[k] = nums[i]
        i += 1
        k += 1

    while j <= high:
        C[k] = nums[j]
        j += 1
        k += 1

    for i, e in enumerate(C):
        nums[low+i] = e


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        counts = [0] * len(nums)
        # 这一步非常重要 把value value index 联系在一起
        # 在更新的时候 还是可以还原到原数组的位置
        nums = [[i, e] for i, e in enumerate(nums)]
        merge_sort(nums, 0, len(nums) - 1, counts)
        return counts


if __name__ == '__main__':
    import random
    nums = random.sample(range(10), 10)
    print(nums)
    print(Solution().countSmaller(nums))

