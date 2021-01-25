"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


105. Construct Binary Tree from Preorder and Inorder Traversal
Medium

4122

110

Add to List

Share
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
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
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        def f(preorder, inorder):
            if not preorder:
                return None
            val = preorder[0]
            i = inorder.index(val)
            root = TreeNode(val)
            root.left = f(preorder[1: i+1], inorder[:i])
            root.right = f(preorder[i+1:], inorder[i+1:])
            return root

        return f(preorder, inorder)


if __name__ == '__main__':
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]

    def visit(root):
        if root:
            yield from visit(root.left)
            yield root.val
            yield from visit(root.right)

    root = Solution().buildTree(preorder, inorder)

    for a, b in zip(visit(root), inorder):
        print(a, b)
        assert a == b

