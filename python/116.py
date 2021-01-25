"""
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000

"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution0:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            if root.left:
                root.left.next = root.right
            if root.right and root.next:
                root.right.next = root.next.left
            root.left = self.connect(root.left)
            root.right = self.connect(root.right)
        return root


# 代码很丑陋

# 注意题干: perfect binary tree

class Solution:
    def connect(self, root: Node) -> Node:
        if root:
            if root.left:
                root.left.next = root.right
                if root.next:
                    root.right.next = root.next.left
                root.left = self.connect(root.left)
                root.right = self.connect(root.right)
        return root



# 一种新的思路 使用了两个参数
# 本质上是树的前序遍历
class Solution:
    def connect(self, root: Node) -> Node:

        def f(a, b):
            if a:
                a.next = b
                f(a.left, a.right)
                if b:
                    f(b.left, b.right)
                    f(a.right, b.left)

        if root:
            f(root.left, root.right)

        return root

