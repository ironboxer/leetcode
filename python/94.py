"""
https://leetcode-cn.com/problems/binary-tree-inorder-traversal/

94. 二叉树的中序遍历
给定一个二叉树的根节点 root ，返回它的 中序 遍历。



示例 1：


输入：root = [1,null,2,3]
输出：[1,3,2]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [1]
输出：[1]
示例 4：


输入：root = [1,2]
输出：[2,1]
示例 5：


输入：root = [1,null,2]
输出：[1,2]


提示：

树中节点数目在范围 [0, 100] 内
-100 <= Node.val <= 100


进阶: 递归算法很简单，你可以通过迭代算法完成吗？


"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def inorder(root):
            if root:
                yield from inorder(root.left)
                yield root.val
                yield from inorder(root.right)

        return list(inorder(root))


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:

        def f(root):
            if root:
                yield from f(root.left)
                yield root.val
                yield from f(root.right)


        return list(f(root))


# 这个解法非常的巧妙

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res



