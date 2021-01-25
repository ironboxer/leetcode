"""
https://leetcode-cn.com/problems/reverse-linked-list-ii/

92. 反转链表 II
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
通过次数85,334提交次数164,971
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    @staticmethod
    def reverse(head):
        cur = None
        while head:
            nxt = head.next
            head.next = cur
            cur = head
            head = nxt
        return cur

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        dummy = ListNode(0, head)
        cur, l = dummy, None
        i = 0
        while cur:
            i += 1
            if i == m:
                l = cur
            elif i == n + 1:
                nxt = cur.next
                cur.next = None
                t = self.reverse(l.next)
                p = t
                while p.next:
                    p = p.next
                p.next = nxt
                l.next = t
                break
            cur = cur.next

        return dummy.next
