"""
https://leetcode.com/problems/path-sum-ii/

Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:

[
   [5,4,11,2],
   [5,8,4,5]
]
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:

        res = []

        def f(root, value, buf):
            if root is None:
                return
            if root.val == value and not (root.left or root.right):
                buf.append(root.val)
                res.append(buf[:])
                buf.pop()
                return
            buf.append(root.val)
            if root.left and root.right:
                f(root.left, value - root.val, buf)
                f(root.right, value - root.val, buf)
            elif root.left:
                f(root.left, value - root.val, buf)
            else:
                f(root.right, value - root.val, buf)
            buf.pop()

        f(root, sum, [])
        return res

# 为什么能过也说不过清楚, 感觉问题出在这里, 改一下能过
