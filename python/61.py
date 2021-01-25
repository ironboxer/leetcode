"""
https://leetcode-cn.com/problems/rotate-list/

61. 旋转链表
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    @staticmethod
    def get_list_len(head):
        r = 0
        while head:
            head = head.next
            r += 1
        return r

    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        total = self.get_list_len(head)
        if total == 0 or k == 0 or k % total == 0:
            return head
        t = (total - k % total)
        cur = head
        while t > 1:
            t -= 1
            cur = cur.next

        nxt = cur.next
        cur.next = None
        cur = nxt
        while cur.next:
            cur = cur.next
        cur.next = head
        return nxt

