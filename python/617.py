"""
https://leetcode-cn.com/problems/merge-two-binary-trees/

617. 合并二叉树
给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。

你需要将他们合并为一个新的二叉树。合并的规则是如果两个节点重叠，那么将他们的值相加作为节点合并后的新值，否则不为 NULL 的节点将直接作为新二叉树的节点。

示例 1:

输入:
	Tree 1                     Tree 2
          1                         2
         / \                       / \
        3   2                     1   3
       /                           \   \
      5                             4   7
输出:
合并后的树:
	     3
	    / \
	   4   5
	  / \   \
	 5   4   7
注意: 合并必须从两个树的根节点开始。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:


        def f(t1, t2):
            if t1 is None and t2 is None:
                return None
            root = TreeNode(0)
            if t1:
                root.val += t1.val
            if t2:
                root.val += t2.val
            root.left = f(t1.left if t1 else None, t2.left if t2 else None)
            root.right = f(t1.right if t1 else None, t2.right if t2 else None)
            return root

        return f(t1, t2)


