"""
https://leetcode.com/problems/binary-search-tree-iterator/

Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.

Calling next() will return the next smallest number in the BST.



Example:



BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false


Note:

next() and hasNext() should run in average O(1) time and uses O(h) memory, where h is the height of the tree.
You may assume that next() call will always be valid, that is, there will be at least a next smallest number in the BST when next() is called.


"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.root = root
        self.it = self._visit()
        self.r = None
        self._next()

    def next(self) -> int:
        """
        @return the next smallest number
        """
        r = self.r
        self._next()
        return r

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.r is not None

    def _visit(self):
        def f(root):
            if root:
                yield from f(root.left)
                yield root.val
                yield from f(root.right)

        return f(self.root)

    def _next(self):
        try:
            self.r = next(self.it)
        except StopIteration:
            self.r = None


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

if __name__ == '__main__':
    pass
