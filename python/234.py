"""
https://leetcode-cn.com/problems/palindrome-linked-list/


234. 回文链表
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        def front_2_end(head):
            while head:
                yield head.val
                head = head.next

        def end_2_front(head):
            if head:
                yield from end_2_front(head.next)
                yield head.val

        for a, b in zip(front_2_end(head), end_2_front(head)):
            if a != b:
                return False
        return True


# TLE

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
        l, r = 0, len(nodes) - 1
        while l < r:
            if nodes[l] != nodes[r]:
                return False
            l += 1
            r -= 1
        return True

# 不合法


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        dummy = ListNode(0, head)
        slow = fast = dummy
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next

        dummy = None
        cur = slow.next
        slow.next = None
        while cur:
            nxt = cur.next
            cur.next = dummy
            dummy = cur
            cur = nxt
        a, b = head, dummy
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next

        return True
