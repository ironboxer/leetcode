"""
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Given the following binary tree:  root = [3,5,1,6,2,0,8,null,null,7,4]



Example 1:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
Output: 3
Explanation: The LCA of nodes 5 and 1 is 3.

Example 2:

Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
Output: 5
Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.


Note:

All of the nodes' values will be unique.
p and q are different and both values will exist in the binary tree.

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    根据性质判断

    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def f(root, node):
            if root:
                if root is node:
                    return True
                return f(root.left, node) or f(root.right, node)
            return False

        def g(root, p, q):
            if p is q:
                return p
            if f(p, q):
                return p
            if f(q, p):
                return q
            if not root:
                return None
            if f(root.left, p) and f(root.left, q):
                return g(root.left, p, q)
            elif f(root.right, p) and f(root.right, q):
                return g(root.right, p, q)
            return root

        return g(root, p, q)




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from functools import lru_cache

class Solution:
    """
    严格按照二叉树的定义来执行
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':


        @lru_cache
        def has(root, node):
            if root is None:
                return False
            if root is node:
                return True
            return has(root.left, node) or has(root.right, node)

        def f(root, p, q):
            if has(p, q):
                return p
            if has(q, p):
                return q
            if has(root.left, p) and has(root.left, q):
                return f(root.left, p, q)
            if has(root.right, p) and has(root.right, q):
                return f(root.right, p, q)
            return root

        return f(root, p, q)

