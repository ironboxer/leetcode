"""
https://leetcode-cn.com/problems/partition-list-lcci/


面试题 02.04. 分割链表
编写程序以 x 为基准分割链表，使得所有小于 x 的节点排在大于或等于 x 的节点之前。如果链表中包含 x，x 只需出现在小于 x 的元素之后(如下所示)。分割元素 x 只需处于“右半部分”即可，其不需要被置于左右两部分之间。

示例:

输入: head = 3->5->8->5->10->2->1, x = 5
输出: 3->1->2->10->5->5->8
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        A, B = [], []
        cur = head
        while cur:
            nxt = cur.next
            cur.next = None
            if cur.val < x:
                if A:
                    A[-1].next = cur
                A.append(cur)
            else:
                if B:
                    B[-1].next = cur
                B.append(cur)
            cur = nxt

        if A and B:
            A[-1].next = B[0]
        if A:
            return A[0]
        if B:
            return B[0]
        return None

