"""
https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof/


剑指 Offer 37. 序列化二叉树
请实现两个函数，分别用来序列化和反序列化二叉树。

示例:

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"
注意：本题与主站 297 题相同：https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def f(root):
            if root is None:
                yield '#'
                return
            yield str(root.val)
            yield from f(root.left)
            yield from f(root.right)

        return ','.join(f(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        items = data.split(',')
        i, total = 0, len(items)

        def f():
            nonlocal i, total
            if i >= total:
                return None
            val = items[i]
            i += 1
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = f()
            root.right = f()
            return root

        return f()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def f(root):
            if root is None:
                yield '#'
                return
            yield str(root.val)
            yield from f(root.left)
            yield from f(root.right)

        return ','.join(f(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        items = data.split(',')
        i, total = 0, len(items)

        def f():
            nonlocal i, total
            if i >= total:
                return None
            val = items[i]
            i += 1
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = f()
            root.right = f()
            return root

        return f()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

