"""
https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/

剑指 Offer 40. 最小的k个数
输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。



示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]
示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]


限制：

0 <= k <= arr.length <= 10000
0 <= arr[i] <= 10000

"""

from typing import List


from heapq import heapify, heappop

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        heapify(arr)
        res = []
        while len(res) < k:
            res.append(heappop(arr))
        return res


from heapq import heapify, heappushpop

# 而 Python 语言中的对为小根堆，因此我们要对数组中所有的数取其相反数，才能使用小根堆维护前 k 小值。
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        nums = [-x for x in arr[:k]]
        heapify(nums)
        while k < len(arr):
            if arr[k] < -nums[0]:
                heappushpop(nums, -arr[k])
            k += 1
        return [-x for x in nums]




def partation(nums, left, right):
    pivot = nums[left]
    while left <= right:
        while left <= right and nums[left] < pivot:
            left += 1
        while left <= right and nums[right] > pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left, right = left + 1, right - 1

    return left


def quick_select(nums, left, right, k):
    if left >= right:
        return

    pivot = partation(nums, left, right)

    if pivot < k:
        quick_select(nums, pivot, right, k)
    elif pivot > k:
        quick_select(nums, left, pivot - 1, k)



# 而 Python 语言中的对为小根堆，因此我们要对数组中所有的数取其相反数，才能使用小根堆维护前 k 小值。
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        quick_select(arr, 0, len(arr) - 1, k)
        return arr[:k]

if __name__ == '__main__':
    nums = [0,0,1,2,4,2,2,3,1,4]
    k = 8
    print(nums, k)
    print(Solution().getLeastNumbers(nums, k))

