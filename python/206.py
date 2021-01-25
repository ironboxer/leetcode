"""
https://leetcode-cn.com/problems/reverse-linked-list/


206. 反转链表
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # 1->2->3
        def f(head):
            if not head or not head.next:
                return head
            nxt = head.next
            head.next = None
            new_head = f(nxt)
            cur = new_head
            while cur.next:
                cur = cur.next
            cur.next = head
            return new_head

        return f(head)
