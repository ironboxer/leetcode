"""
https://leetcode-cn.com/problems/recover-binary-search-tree/

99. 恢复二叉搜索树
给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。

进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？



示例 1：


输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
示例 2：


输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。


提示：

树上节点的数目在范围 [2, 1000] 内
-231 <= Node.val <= 231 - 1

"""



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev, a, b = None, None, None

        def inorder(root):
            if root is None:
                return
            nonlocal a, b, prev
            inorder(root.left)
            if prev is not None and prev.val > root.val:
                if a is None:
                    a = prev
                b = root
            prev = root
            inorder(root.right)

        inorder(root)

        a.val, b.val = b.val, a.val



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def f(root):
            if root:
                yield from f(root.left)
                yield root
                yield from f(root.right)

        # 最重要的是pre节点的存在
        # a 用来记录最早的那个节点 b用来记录最晚的那个节点
        # pre用来记录走过的每一个节点
        # 没有搞懂 两个节点有错误到底意味着什么
        pre, a, b = None, None, None
        for node in f(root):
            if pre and pre.val > node.val:
                if not a:
                    a = pre
                b = node
            pre = node

        a.val, b.val = b.val, a.val

