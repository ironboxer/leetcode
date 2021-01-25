"""
https://leetcode.com/problems/binary-tree-paths/

Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3

"""

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        res = []

        def f(root, path):
            if not root:
                return
            path.append(root.val)
            if not root.left and not root.right:
                res.append(path[:])
                return

            if root.left:
                a = path[:]
                f(root.left, a)
            if root.right:
                b = path[:]
                f(root.right, b)

        f(root, [])

        return ['->'.join(map(str, items)) for items in res]


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    print(Solution().binaryTreePaths(root))

