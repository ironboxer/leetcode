"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/


Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # 二叉树的后序遍历
        def f(root):
            if root:
                yield from f(root.right)
                yield from f(root.left)
                yield root

        dummy = None
        for node in f(root):
            node.left = None
            node.right = dummy
            dummy = node

        return dummy


# 另一种方法
class Solution:
    def flatten(self, root: TreeNode) -> None:
        def f(root):
            if root:
                f(root.left)
                f(root.right)
                left, right = root.left, root.right
                root.left, root.right = None, left
                # 把新接入的left的最后一个元素的right指向已经排好序的right节点
                while root.right:
                    root = root.right
                root.right = right
        f(root)
        return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)

    r = Solution().flatten(root)
    while r:
        print(r.val)
        r = r.right

