"""
https://leetcode.com/problems/merge-k-sorted-lists

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.

"""

# Definition for singly-linked list.

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        lists = [node for node in lists if node]
        dummy = ListNode(0)
        cur = dummy
        while lists:
            min_val, min_pos = 2 ** 31, -1
            for i, node in enumerate(lists):
                if node.val < min_val:
                    min_val = node.val
                    min_pos = i
            cur.next = lists[min_pos]
            cur = cur.next
            lists[min_pos] = lists[min_pos].next
            if lists[min_pos] is None:
                lists.pop(min_pos)
        return dummy.next


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        from queue import PriorityQueue
        dummy = ListNode(0, None)
        cur = dummy
        q = PriorityQueue()
        for i, node in enumerate(lists):
            if node:
                q.put((node.val, i, node))
        while q.qsize() > 0:
            node = q.get()
            idx = node[1]
            cur.next = node[-1]
            cur = cur.next
            # 很好的控制了队列的大小
            if cur.next:
                q.put((cur.next.val, idx, cur.next))
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        lists = list(filter(None, lists))
        while lists:
            j = 0
            for i in range(1, len(lists)):
                if lists[i].val <= lists[j].val:
                    j = i
            cur.next = lists[j]
            cur = cur.next
            lists[j] = lists[j].next
            if not lists[j]:
                lists.pop(j)

        return dummy.next



from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                # TODO: 这里为什么会报错?
                q.put((node.val, node))
        while not q.empty():
            _, node = q.get()
            cur.next = node
            cur = cur.next
            if node.next:
                q.put((node.next.val, node.next))
        return dummy.next


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        q = PriorityQueue()
        for i, node in enumerate(lists):
            if node:
                q.put((node.val, i))
        while not q.empty():
            _, i = q.get()
            cur.next = lists[i]
            cur = cur.next
            if lists[i].next:
                lists[i] = lists[i].next
                q.put((lists[i].val, i))
        return dummy.next



if __name__ == '__main__':
    l1 = ListNode(1, ListNode(4, ListNode(5)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    l3 = ListNode(2, ListNode(6))
    lists = [l1, l2, l3]

    cur = Solution().mergeKLists(lists)
    while cur:
        print(cur.val)
        cur = cur.next


