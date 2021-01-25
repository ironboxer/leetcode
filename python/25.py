"""
https://leetcode-cn.com/problems/reverse-nodes-in-k-group/

25. K 个一组翻转链表
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。



示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5



说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def count(head):
        cnt = 0
        while head:
            cnt += 1
            head = head.next
        return cnt


    @staticmethod
    def reverse(head):
        cur = None
        while head:
            nxt = head.next
            head.next = cur
            cur = head
            head = nxt
        return cur

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        n = self.count(head)
        if k == n:
            return self.reverse(head)

        dummy = ListNode(0, head)
        i = 0
        l, r = dummy, head
        while r:
            i += 1
            nxt = r.next
            if i % k == 0:
                r.next = None
                h = self.reverse(l.next)
                l.next = h
                while h.next:
                    h = h.next
                h.next = nxt
                l = h
            r = nxt

        return dummy.next
