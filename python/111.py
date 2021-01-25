"""
https://leetcode.com/problems/minimum-depth-of-binary-tree/


Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: TreeNode) -> int:

        def f(root):
            if root is None:
                return 0
            if root.left is None:
                return f(root.right) + 1
            if root.right is None:
                return f(root.left) + 1
            return min(f(root.left), f(root.right)) + 1

        return f(root)

# 需要仔细读一下题目, 看一下题目问的是啥?



class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        is_leaf = lambda x: x and not x.left and not x.right
        from collections import deque
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if is_leaf(node):
                return depth
            if node.left:
                queue.append((node.right, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return depth

