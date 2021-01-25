"""
binary tree visit operation
preorder, inorder, postorder, levelorder
"""


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def preorder(root):
    if root:
        yield root
        yield from preorder(root.left)
        yield from preorder(root.right)


def inorder(root):
    if root:
        yield from inorder(root.left)
        yield root
        yield from inorder(root.right)


def postorder(root):
    if root:
        yield from postorder(root.left)
        yield from postorder(root.right)
        yield root


def levelorder(root):
    from collections import deque
    queue = deque([root])
    while queue:
        node = queue.popleft()
        yield node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)


def stack_preorder(root):
    print('stack_preorder')
    stack = [root]
    while stack:
        node = stack.pop()
        yield node
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


def stack_inorder(root):
    print('stack inorder')
    stack = []
    cur = root
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        yield cur
        cur = cur.right


def stack_postorder(root):
    print('stack postorder')
    stack = []
    cur = root
    prev = None
    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        # NOTE: 因为是抄的别人的代码 所以不知道怎么改
        if stack:
            cur = stack.pop()
            if not cur.right or pre  == cur.right:
                yield cur
                pre = cur
                cur = None
            else:
                stack.append(cur)
                cur = cur.right


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    for node in preorder(root):
        print(node.val)
    print('-' * 100)

    for node in inorder(root):
        print(node.val)
    print('-' * 100)

    for node in postorder(root):
        print(node.val)
    print('-' * 100)

    for node in levelorder(root):
        print(node.val)
    print('-' * 100)

    for node in stack_preorder(root):
        print(node.val)
    print('-' * 100)

    for node in stack_inorder(root):
        print(node.val)
    print('-' * 100)

    for node in stack_postorder(root):
        print(node.val)
    print('-' * 100)

