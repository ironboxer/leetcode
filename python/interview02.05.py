"""
https://leetcode-cn.com/problems/sum-lists-lcci/

面试题 02.05. 链表求和
给定两个用链表表示的整数，每个节点包含一个数位。

这些数位是反向存放的，也就是个位排在链表首部。

编写函数对这两个整数求和，并用链表形式返回结果。



示例：

输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
输出：2 -> 1 -> 9，即912
进阶：思考一下，假设这些数位是正向存放的，又该如何解决呢?

示例：

输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
输出：9 -> 1 -> 2，即912
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            val = l1.val + l2.val + carry
            cur.next = ListNode(val % 10)
            carry = val // 10
            cur = cur.next
            l1, l2 = l1.next, l2.next

        while l1:
            val = l1.val + carry
            cur.next = ListNode(val % 10)
            carry = val // 10
            cur = cur.next
            l1 = l1.next

        while l2:
            val = l2.val + carry
            cur.next = ListNode(val % 10)
            carry = val // 10
            cur = cur.next
            l2 = l2.next

        if carry:
            cur.next = ListNode(carry)

        return dummy.next

