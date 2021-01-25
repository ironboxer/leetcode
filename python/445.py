"""
https://leetcode-cn.com/problems/add-two-numbers-ii/

445. 两数相加 II
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。



进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。



示例：

输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        A, B = [], []
        while l1:
            A.append(l1)
            l1 = l1.next
        while l2:
            B.append(l2)
            l2 = l2.next
        cur = None
        i, j = len(A) - 1, len(B) - 1
        t = 0
        while i >= 0 and j >= 0:
            r = A[i].val + B[j].val + t
            t = r // 10
            node = ListNode(r % 10, cur)
            cur = node
            i, j = i - 1, j - 1

        while i >= 0:
            r = A[i].val + t
            t = r // 10
            node = ListNode(r % 10, cur)
            cur = node
            i -= 1

        while j >= 0:
            r = B[j].val + t
            t = r // 10
            node = ListNode(r % 10, cur)
            cur = node
            j -= 1

        if t > 0:
            node = ListNode(t, cur)
            cur = node

        return cur

# 不要忘记进位
