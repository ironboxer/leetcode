"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return '<Node:%d>' % self.val


class Solution1:
    def maxPathSum(self, root: TreeNode) -> int:
        max_sum = None

        def f(root):
            if root:
                a = f(root.left)
                b = f(root.right)
                c = root.val
                v = max(c, a + c, b + c, a + b + c)
                nonlocal max_sum
                if max_sum is None:
                    max_sum = v
                else:
                    max_sum = max(max_sum, v)
                print(
                    "c:%d, a+c:%d, b+c:%d, a+b+c:%d, max_sum:%d" % (
                        c, a + c, b + c, a + b + c, max_sum
                    )
                )
                return max(c, a + c, b + c)
            return 0

        f(root)
        return max_sum


class Solution2:

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_val = -999999

        def f(root):
            if not root:
                return 0
            v, l, r = root.val, f(root.left), f(root.right)
            t = max(v, l + v, r + v, l + r + v)
            self.max_val = max(self.max_val, t)
            return max(v, l + v, r + v)

        f(root)

        return self.max_val


class Solution3:
    def maxPathSum(self, root: TreeNode) -> int:
        res = -999999

        def f(root):
            if not root:
                return 0
            # 因为root存在, 所以子树不应该返回小于0的结果, 这样的结果应该被过滤掉
            v, l, r = root.val, max(0, f(root.left)), max(0, f(root.right))
            nonlocal res
            res = max(res, v + l + r)
            return max(l, r) + v

        f(root)

        return res


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        res = -999999

        def f(root):
            if not root:
                return 0
            l, r = f(root.left), f(root.right)
            nonlocal res
            # 这里的意思就是从左到右, 只允许两个分叉, 中间用根节点连接
            res = max(res, l + r + root.val)
            return max(max(l, r) + root.val, 0)

        f(root)
        return res


# 为啥这个就过了呢?
# 没有看懂这道题, 有点模糊

# 题目要求的是最大路径和，而不是最大子树和
# 最大路径和就是一个一笔画问题。


if __name__ == '__main__':
    root = TreeNode(-3)
    print(Solution().maxPathSum(root))

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left.right = TreeNode(1)
    print(Solution().maxPathSum(root))
    # [5,4,8,11,null,13,4,7,2,null,null,null,1]
