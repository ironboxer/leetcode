"""
https://leetcode.com/problems/sliding-window-maximum/

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:

Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7


Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length

"""

from typing import List


# 把时间复杂度从O(kn)降低到O(n)

# queue的设计思路
# queue[0]保存当期buffer中的最大元素 queue[-1]保存当前队列中的最新的元素
# 每来一个新的元素 就检测队列中比这个元素小的, 然后弹出
# 然后将这个元素加入队列
# 检测队列头部的元素是否为已经超出范围, 如果超出范围 就弹出.
# 思路是十分清晰的


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        queue = deque()
        res = []
        for i, e in enumerate(nums):
            # 这个地方的平摊时间复杂度就是O(n)
            while queue and nums[queue[-1]] < e:
                queue.pop()
            if queue and queue[0] + k <= i:
                queue.popleft()
            queue.append(i)
            print(i, e, queue)
            if i >= k - 1:
                # 始终保证queue[0]是当前队列的最大元素
                res.append(nums[queue[0]])

        return res

# 复杂度分析?

# 大概就是这个样子
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        res = []
        q = deque()
        for i, e in enumerate(nums):
            while q and nums[q[-1]] < e:
                q.pop()
            while q and q[0] + k <= i:
                q.popleft()
            q.append(i)
            if i >= k-1:
                res.append(nums[q[0]])

            if len(q) > k:
                q.popleft()
        return res


from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        window = deque()
        for i, e in enumerate(nums):
            while window and nums[window[-1]] < e:
                window.pop()
            while window and i - window[0] >= k:
                window.popleft()
            window.append(i)
            if i + 1 >= k:
                res.append(nums[window[0]])

        return res


if __name__ == '__main__':

    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(Solution().maxSlidingWindow(nums, k))


    nums = [1, -1]
    k = 1
    print(Solution().maxSlidingWindow(nums, k))

    nums = [5, 3, 4]
    k = 1
    print(Solution().maxSlidingWindow(nums, k))
