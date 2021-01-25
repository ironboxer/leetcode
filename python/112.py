"""
https://leetcode.com/problems/path-sum/

Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def f(root, value):
            if root is None:
                # 从来没有走这里
                print('hit')
                return value == 0
            if value == root.val and root.left is None and root.right is None:
                return True
            if root.left and root.right:
                return f(root.left, value - root.val) or f(root.right, value - root.val)
            elif root.left:
                return f(root.left, value - root.val)
            elif root.right:
                return f(root.right, value - root.val)
            return False

        return f(root, sum) if root else False


# 这个版本是一个更加贴近原题的方案
class Solution0:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def f(root, value):
            if root is None:
                return False
            if value == root.val and root.left is None and root.right is None:
                return True
            if root.left and root.right:
                return f(root.left, value - root.val) or f(root.right, value - root.val)
            elif root.left:
                return f(root.left, value - root.val)
            elif root.right:
                return f(root.right, value - root.val)
            return False

        return f(root, sum)


# 二叉树这个有点烦

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    print(Solution().hasPathSum(root, 1))

    root = TreeNode(-2)
    root.right = TreeNode(-3)
    print(Solution().hasPathSum(root, -5))
