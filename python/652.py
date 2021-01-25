"""
https://leetcode.com/problems/find-duplicate-subtrees/

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.



Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]


Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        res = []
        path = {}
        visited = set()
        def f(root):
            if not root:
                return '#'
            l, r = f(root.left), f(root.right)
            p = l + ',' + r + ',' + str(root.val)
            path[root] = p
            return p

        f(root)

        nodes = [node for node in path]
        # 这个双层循环有改进的空间
        for i in range(len(nodes) - 1):
            for j in range(i+1, len(nodes)):
                a, b = nodes[i], nodes[j]
                if path[a] == path[b]:
                    if path[a] in visited:
                        continue
                    visited.add(path[a])
                    res.append(a)
        return res


# 之前已经做过n次 但是现在又不会了


if __name__ == '__main__':
    root = TreeNode(1)

    root.left = TreeNode(2)
    root.left.left = TreeNode(4)

    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(4)
    root.right.right = TreeNode(4)

    res = Solution().findDuplicateSubtrees(root)
    for node in res:
        print(node.val)

