"""
https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cnt = {}
        cur = head
        while cur:
            cnt[cur.val] = cnt.get(cur.val, 0) + 1
            cur = cur.next

        dummy = ListNode(0)
        cur = dummy
        while head:
            nxt = head.next
            head.next = None
            if cnt[head.val] == 1:
                cur.next = head
                cur = cur.next
            head = nxt

        return dummy.next


if __name__ == '__main__':
    pass
