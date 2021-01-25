"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/

Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

Example:

You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
Clarification: The above format is the same as how LeetCode serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.

Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.


# preorder: 1 2 3 4 5
# inorder : 2 1 4 3 5

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        def f(root):
            if not root:
                yield '#'
            else:
                yield str(root.val)
                yield from f(root.left)
                yield from f(root.right)

        return ','.join(f(root)) if root else ''


    def deserialize(self, data):
        if not data:
            return None

        def f():
            val = next(it)
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = f()
            root.right= f()
            return root

        nodes = data.split(',')
        it = iter(nodes)

        return f()


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))



class Codec:
    """
    preoder
    """
    def serialize(self, root):
        def f(root):
            if root:
                yield root.val
                yield from f(root.left)
                yield from f(root.right)
            else:
                yield '#'

        return ','.join(map(str, f(root)))


    def deserialize(self, data):
        from collections import deque
        vals = data.split(',')
        queue = deque(vals)

        def f():
            if not queue:
                return None
            val = queue.popleft()
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.left = f()
            root.right = f()
            return root

        return f()



class Codec:
    """
    postorder
    """
    def serialize(self, root):
        def f(root):
            if root:
                yield from f(root.left)
                yield from f(root.right)
                yield root.val
            else:
                yield '#'

        return ','.join(map(str, f(root)))


    def deserialize(self, data):
        vals = data.split(',')
        def f():
            if not vals:
                return None
            val = vals.pop()
            if val == '#':
                return None
            root = TreeNode(int(val))
            root.right = f()
            root.left = f()
            return root

        return f()



class Codec:
    """
    levelorder
    """
    def serialize(self, root):
        vals = []
        from collections import deque
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                vals.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                vals.append('#')

        return ','.join(vals)

    def deserialize(self, data):
        from collections import deque
        vals = deque(data.split(','))
        if not vals or vals[0] == '#':
            return None
        root = TreeNode(int(vals.popleft()))
        # 需要暂存父节点
        queue = deque([root])
        while queue:
            parent = queue.popleft()
            l, r = vals.popleft(), vals.popleft()
            parent.left = TreeNode(int(l)) if l != '#' else None
            parent.right = TreeNode(int(r)) if r != '#' else None
            if parent.left:
                queue.append(parent.left)
            if parent.right:
                queue.append(parent.right)

        return root


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(6)
    root.right.left.right = TreeNode(7)

    def inorder_visit(root):
        if root:
            inorder_visit(root.left)
            print(root.val)
            inorder_visit(root.right)

    c = Codec()
    data = c.serialize(root)
    print(data)
    tree = c.deserialize(data)
    inorder_visit(tree)

