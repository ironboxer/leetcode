"""
https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

145. 二叉树的后序遍历
给定一个二叉树，返回它的 后序 遍历。

示例:

输入: [1,null,2,3]
   1
    \
     2
    /
   3

输出: [3,2,1]
进阶: 递归算法很简单，你可以通过迭代算法完成吗？
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        def f(root):
            if root:
                yield from f(root.left)
                yield from f(root.right)
                yield root.val


        return list(f(root))



from collections import deque


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        queue = deque()
        stack = [root]
        while stack:
            root = stack.pop()
            queue.appendleft(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return list(queue)



# 这道题的解法非常巧妙
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]
        while stack:
            root = stack.pop()
            res.append(root.val)
            if root.left:
                stack.append(root.left)
            if root.right:
                stack.append(root.right)

        return res[::-1]
