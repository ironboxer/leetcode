"""
https://leetcode-cn.com/problems/linked-list-random-node/


382. 链表随机节点
给定一个单链表，随机选择链表的一个节点，并返回相应的节点值。保证每个节点被选的概率一样。

进阶:
如果链表十分大且长度未知，如何解决这个问题？你能否使用常数级空间复杂度实现？

示例:

// 初始化一个单链表 [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom()方法应随机返回1,2,3中的一个，保证每个元素被返回的概率相等。
solution.getRandom();
"""


import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        res = 0
        cnt = 1
        cur = self.head
        while cur is not None:
            cnt += 1
            if random.randrange(cnt) == 0:
                res = cur.val

            cur = cur.next

        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random

class Solution:

    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        res = 0
        cnt = 0
        cur = self.head
        # 因为需要遍历全部的元素 所以时间复杂度为O(n)
        # 所以本质上是用时间换空间的解法
        while cur is not None:
            cnt += 1
            # 这里实际上像是一种采样方式
            # 随机的范围随着遍历元素的增多而变大
            if random.randrange(cnt) == 0:
                res = cur.val
            cur = cur.next

        return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
