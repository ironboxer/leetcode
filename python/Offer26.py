"""
https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/

剑指 Offer 26. 树的子结构
输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)

B是A的子结构， 即 A中有出现和B相同的结构和节点值。

例如:
给定的树 A:

     3
    / \
   4   5
  / \
 1   2
给定的树 B：

   4
  /
 1
返回 true，因为 B 与 A 的一个子树拥有相同的结构和节点值。

示例 1：

输入：A = [1,2,3], B = [3,1]
输出：false
示例 2：

输入：A = [3,4,5,1,2], B = [4,1]
输出：true
限制：

0 <= 节点个数 <= 10000
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        if B is None:
            return False

        def f(a, b, flag=True):
            if b is None:
                return True
            if a is None:
                return False

            if flag:
                if a.val == b.val and f(a.left, b.left, False) and f(a.right, b.right, False):
                    return True
                return f(a.left, b) or f(a.right, b)
            else:
                return a.val == b.val and f(a.left, b.left, False) and f(a.right, b.right, False)

            # if a.val == b.val:
            #     if f(a.left, a.left, True) and f(a.right, b.right, True):
            #         return True
            # if not flag:
            #     return f(a.left, b, flag) or f(a.right, b, flag)
            # return False

        return f(A, B)


