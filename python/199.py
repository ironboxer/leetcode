"""
https://leetcode-cn.com/problems/binary-tree-right-side-view/

199. 二叉树的右视图
给定一棵二叉树，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

示例:

输入: [1,2,3,null,5,null,4]
输出: [1, 3, 4]
解释:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:

        def f(root):
            if root:
                yield root.val
                yield from f(root.right)

        return list(f(root))


from collections import deque

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res = []
        queue = deque([(root, 0)])
        while queue:
            node, level = queue.popleft()
            if level >= len(res):
                res.append([])
            res[level].append(node.val)
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return [item[-1] for item in res]

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)

    print(Solution().rightSideView(root))

