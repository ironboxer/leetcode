"""
https://leetcode-cn.com/problems/path-sum-iii/

437. 路径总和 III
给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

示例：

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
"""



# slow but work
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        res = []

        def f(root, path):
            if root is None:
                return
            path.append(root.val)
            if sum(path) == target:
                res.append(path[:])
            f(root.left, path[:])
            f(root.right, path[:])

        def g(root):
            if root:
                yield root
                yield from g(root.left)
                yield from g(root.right)

        for node in g(root):
            f(node, [])

        return len(res)

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> int:
        self.res = 0

        def f(root, s, flag):
            if root is None:
                return
            if s == root.val:
                self.res += 1
            f(root.left, s - root.val, False)
            f(root.right, s - root.val, False)
            if flag:
                f(root.left, s, flag)
                f(root.right, s, flag)

        f(root, target, True)

        return self.res

