"""
https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/

958. 二叉树的完全性检验
给定一个二叉树，确定它是否是一个完全二叉树。

百度百科中对完全二叉树的定义如下：

若设二叉树的深度为 h，除第 h 层外，其它各层 (1～h-1) 的结点数都达到最大个数，第 h 层所有的结点都连续集中在最左边，这就是完全二叉树。（注：第 h 层可能包含 1~ 2h 个节点。）



示例 1：



输入：[1,2,3,4,5,6]
输出：true
解释：最后一层前的每一层都是满的（即，结点值为 {1} 和 {2,3} 的两层），且最后一层中的所有结点（{4,5,6}）都尽可能地向左。
示例 2：



输入：[1,2,3,4,5,null,7]
输出：false
解释：值为 7 的结点没有尽可能靠向左侧。


提示：

树中将会有 1 到 100 个结点。

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque


class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root is None:
            return True

        queue = deque([(root, 1)])
        last = 0
        while queue:
            node, i = queue.popleft()
            if last + 1 != i:
                return False
            last = i
            if node.left:
                queue.append((node.left, i * 2))
            if node.right:
                queue.append((node.right, i * 2 + 1))

        return True

