"""
https://leetcode-cn.com/problems/remove-linked-list-elements/

203. 移除链表元素
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next:
            nxt = cur.next
            if nxt.val == val:
                cur.next = nxt.next
            else:
                cur = nxt

        return dummy.next

