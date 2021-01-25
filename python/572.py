"""
https://leetcode-cn.com/problems/subtree-of-another-tree/


572. 另一个树的子树
给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

示例 1:
给定的树 s:

     3
    / \
   4   5
  / \
 1   2
给定的树 t：

   4
  / \
 1   2
返回 true，因为 t 与 s 的一个子树拥有相同的结构和节点值。

示例 2:
给定的树 s：

     3
    / \
   4   5
  / \
 1   2
    /
   0
给定的树 t：

   4
  / \
 1   2
返回 false。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def f(s, t, flag=False):
            if s is None and t is None:
                return True
            if s is None or t is None:
                return False
            if s.val == t.val:
                if f(s.left, t.left, True) and f(s.right, t.right, True):
                    return True
            if flag:
                return False
            return f(s.left, t, flag) or f(s.right, t, flag)

        return f(s, t)

