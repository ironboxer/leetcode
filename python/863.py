"""
https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/

863. 二叉树中所有距离为 K 的结点
给定一个二叉树（具有根结点 root）， 一个目标结点 target ，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。



示例 1：

输入：root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
输出：[7,4,1]
解释：
所求结点为与目标结点（值为 5）距离为 2 的结点，
值分别为 7，4，以及 1



注意，输入的 "root" 和 "target" 实际上是树上的结点。
上面的输入仅仅是对这些对象进行了序列化描述。


提示：

给定的树是非空的。
树上的每个结点都具有唯一的值 0 <= node.val <= 500 。
目标结点 target 是树上的结点。
0 <= K <= 1000.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Node:
    def __init__(self, x, left=None, right=None, parent=None, visited=False):
        self.val = x
        self.left = left
        self.right = right
        self.parent = parent
        self.visited = False

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        res = []
        new_target = None
        def f(root, parent=None):
            if root is None:
                return None
            new_root = Node(root.val, parent=parent)
            if root.left is not None:
                new_root.left = f(root.left, new_root)
            if root.right is not None:
                new_root.right = f(root.right, new_root)
            if root is target:
                nonlocal new_target
                new_target = new_root

            return new_root

        def h(node, level=0):
            if node is None or node.visited:
                return
            node.visited = True
            if level == K:
                res.append(node.val)
                return
            h(node.left, level + 1)
            h(node.right, level + 1)
            h(node.parent, level + 1)
            node.visited = False

        f(root)
        h(new_target)

        return res

