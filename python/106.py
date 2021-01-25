"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

106. Construct Binary Tree from Inorder and Postorder Traversal
Medium

2147

41

Add to List

Share
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:

        def f(inorder, postorder):
            if not inorder:
                return None
            val = postorder[-1]
            i = inorder.index(val)
            root = TreeNode(val)
            root.left = f(inorder[:i], postorder[:i])
            root.right = f(inorder[i+1:], postorder[i:-1])
            return root

        return f(inorder, postorder)


if __name__ == '__main__':
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]

    def visit(root):
        if root:
            yield from visit(root.left)
            yield root.val
            yield from visit(root.right)

    root = Solution().buildTree(inorder, postorder)

    for a, b in zip(visit(root), inorder):
        print(a, b)
        assert a == b

