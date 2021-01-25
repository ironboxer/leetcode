"""
https://leetcode-cn.com/problems/shu-zu-zhong-de-ni-xu-dui-lcof/


剑指 Offer 51. 数组中的逆序对
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。



示例 1:

输入: [7,5,6,4]
输出: 5


限制：

0 <= 数组长度 <= 50000


"""

from typing import List


def merge_sort(nums, left, right):
    if left >= right:
        return 0

    counter = 0

    mid = (left + right) // 2
    counter += merge_sort(nums, left, mid)
    counter += merge_sort(nums, mid+1, right)
    tmp = [0] * (right - left + 1)
    i, j, k = left, mid + 1, 0
    while i <= mid and j <= right:
        if nums[i] <= nums[j]:
            # NOTE: j 偏离 mid + 1 的位置表示 left part 中有大于nums[j]的元素存在
            # 才使得 j 逐渐偏离 (mid + 1)
            counter += j - (mid + 1)
            tmp[k] = nums[i]
            i += 1
        else:
            tmp[k] = nums[j]
            j += 1
        k += 1
    while i <= mid:
        counter += j - (mid + 1)
        tmp[k] = nums[i]
        i += 1
        k += 1
    while j <= right:
        tmp[k] = nums[j]
        j += 1
        k += 1
    for p in range(k):
        nums[left + p] = tmp[p]

    return counter


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        return merge_sort(nums, 0, len(nums) - 1)



if __name__ == '__main__':
    #nums = [7,5,6,4]
    nums = [1,2,3,4,5,6,7,8,9,10]
    print(nums)
    print(Solution().reversePairs(nums))
    print(nums)
