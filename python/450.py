"""
https://leetcode-cn.com/problems/delete-node-in-a-bst/


450. 删除二叉搜索树中的节点
给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。

一般来说，删除节点可分为两个步骤：

首先找到需要删除的节点；
如果找到了，删除它。
说明： 要求算法时间复杂度为 O(h)，h 为树的高度。

示例:

root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

给定需要删除的节点值是 3，所以我们首先找到 3 这个节点，然后删除它。

一个正确的答案是 [5,4,6,2,null,null,7], 如下图所示。

    5
   / \
  4   6
 /     \
2       7

另一个正确答案是 [5,2,6,null,4,null,7]。

    5
   / \
  2   6
   \   \
    4   7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        isleaf = lambda x: x.left is None and x.right is None

        def f(root, node):
            if root is None:
                return
            if root.left is node:
                if isleaf(node):
                    root.left = None
                else:
                    if node.left is None:
                        root.left = node.right
                    elif node.right is None:
                        root.left = node.left
                    else:
                        cur = node.left
                        while cur.right:
                            cur = cur.right
                        cur.right = node.right
                        root.left = node.left
            elif root.right is node:
                if isleaf(node):
                    root.right = None
                else:
                    if node.left is None:
                        root.right = node.right
                    elif node.right is None:
                        root.right = node.left
                    else:
                        cur = node.right
                        while cur.left:
                            cur = cur.left
                        cur.left = node.left
                        root.right = node.right
            else:
                f(root.left, node)
                f(root.right, node)


        def g(root, val):
            if root is None:
                return None
            if root.val == val:
                return root
            return g(root.left, val) or g(root.right, val)


        while True:
            node = g(root, key)
            if node is None:
                break
            if node is root:
                if isleaf(root):
                    return None
                elif root.left is None:
                    root = root.right
                elif root.right is None:
                    root = root.left
                else:
                    cur = root.left
                    while cur.right:
                        cur = cur.right
                    cur.right = root.right
                    root = root.left
            else:
                f(root, node)

        return root


if __name__ == '__main__':

    def preorder(root):
        if root:
            print(root.val)
            preorder(root.left)
            preorder(root.right)


    root = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.right = TreeNode(4)
    preorder(root)
    print()

    root = Solution().deleteNode(root, 2)
    preorder(root)

