"""
https://leetcode.com/problems/house-robber-iii/

The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example 1:

Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \
     3   1

Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
Example 2:

Input: [3,4,5,1,3,null,1]

     3
    / \
   4   5
  / \   \
 1   3   1

Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

"""



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution0:
    """
    according to defination
    """
    def rob(self, root: TreeNode) -> int:

        def f(root):
            if not root:
                return 0
            val = 0
            if root.left:
                val += f(root.left.left) + f(root.left.right)
            if root.right:
                val += f(root.right.left) + f(root.right.right)

            return max(val + root.val, f(root.left) + f(root.right))

        return f(root)


class Solution1:
    def rob(self, root: TreeNode) -> int:
        memo = {}

        def f(root):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            val = 0
            if root.left:
                val += f(root.left.left) + f(root.left.right)
            if root.right:
                val += f(root.right.left) + f(root.right.right)

            max_val = max(val + root.val, f(root.left) + f(root.right))
            memo[root] = max_val
            return max_val

        return f(root)


class Solution:
    def rob(self, root: TreeNode) -> int:

        def f(root):
            if not root:
                return [0, 0]
            a, b = f(root.left), f(root.right)
            # 这个递归的结构有点难以理解
            return [max(a) + max(b), root.val + a[0] + b[0]]

        return max(f(root))





























class Solution:
    """
    太过高级的算法实际上已经超出的你的理解能力了
    需要循序渐进
    """
    def rob(self, root: TreeNode) -> int:

        """
        这个算法虽然慢但是有效
        是完全按照题意来的
        所以是正确的
        """
        def f(root):
            if not root:
                return 0
            l, r = f(root.left), f(root.right)
            val = root.val
            if root.left:
                val += f(root.left.left) + f(root.left.right)
            if root.right:
                val += f(root.right.left) + f(root.right.right)

            return max(val, l +  r)

        return f(root)


class Solution:
    def rob(self, root: TreeNode) -> int:

        """
        这个算法其实更加抽象

        或者去类别 House Robber 这道题的不用数组的dp方式
        """
        def f(root):
            if not root:
                return 0, 0

            l, r = f(root.left), f(root.right)

            # 包含roor节点的最大值  不包含root节点的最大值
            return root.val + l[1] + r[1], max(l) + max(r)


        return max(f(root))
















# Another Slow But Work


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from functools import lru_cache

class Solution:
    def rob(self, root: TreeNode) -> int:

        @lru_cache
        def f(root):
            if root is None:
                return 0
            val = root.val
            if root.left:
                val += f(root.left.left) + f(root.left.right)
            if root.right:
                val += f(root.right.left) + f(root.right.right)

            return max(val, f(root.left) + f(root.right))

        return f(root)




if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)

    print(Solution().rob(root))


    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(1)

    print(Solution().rob(root))

