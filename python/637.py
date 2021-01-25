"""
https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/

637. 二叉树的层平均值
给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。



示例 1：

输入：
    3
   / \
  9  20
    /  \
   15   7
输出：[3, 14.5, 11]
解释：
第 0 层的平均值是 3 ,  第1层是 14.5 , 第2层是 11 。因此返回 [3, 14.5, 11] 。


提示：

节点值的范围在32位有符号整数范围内。

"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []

        def f(root, level):
            if root is None:
                return
            if level >= len(res):
                res.append([])
            res[level].append(root.val)
            f(root.left, level + 1)
            f(root.right, level + 1)

        f(root, 0)

        return [sum(items) / len(items) for items in res]


