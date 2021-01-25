"""
https://leetcode-cn.com/problems/reorder-list/


143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        n = len(nodes)
        res = []
        for i in range(n//2):
            res.append(nodes[i])
            res.append(nodes[n-1-i])
        if n & 1:
            res.append(nodes[n // 2])
        assert len(nodes) == len(res)
        for i in range(n-1):
            res[i].next = res[i+1]
        res[n-1].next = None


if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    cur = head

    while cur:
        print(cur.val, end='\t')
        cur = cur.next
    print()

    Solution().reorderList(head)

    cur = head
    while cur:
        print(cur.val, end='\t')
        cur = cur.next
    print()

