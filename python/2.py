"""
https://leetcode-cn.com/problems/add-two-numbers/

2. 两数相加
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        base = 0
        while l1 and l2:
            val = l1.val + l2.val + base
            cur.next = ListNode(val % 10)
            base = val // 10
            cur = cur.next
            l1, l2 = l1.next, l2.next
        l = l1 or l2
        while l:
            val = l.val + base
            cur.next = ListNode(val % 10)
            base = val // 10
            cur = cur.next
            l = l.next
        if base > 0:
            cur.next = ListNode(base)
        return dummy.next
