"""
https://leetcode-cn.com/problems/longest-univalue-path/


687. 最长同值路径
给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。

注意：两个节点之间的路径长度由它们之间的边数表示。

示例 1:

输入:

              5
             / \
            4   5
           / \   \
          1   1   5
输出:

2
示例 2:

输入:

              1
             / \
            4   5
           / \   \
          4   4   5
输出:

2
注意: 给定的二叉树不超过10000个结点。 树的高度不超过1000。

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        res = 0

        def f(root):
            nonlocal res
            if not root:
                return 0
            l, r = f(root.left), f(root.right)
            a = l + 1 if root.left and root.left.val == root.val else 0
            b = r + 1 if root.right and root.right.val == root.val else 0
            res = max(res, a + b)
            return max(a, b)

        f(root)
        return res


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(5)

    print(Solution().longestUnivaluePath(root))

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(1)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)

    print(Solution().longestUnivaluePath(root))


    root = TreeNode(1)
    root.right = TreeNode(1)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(1)
    root.right.left.left = TreeNode(1)
    root.right.left.right = TreeNode(1)
    root.right.right.left = TreeNode(1)

    print(Solution().longestUnivaluePath(root))

