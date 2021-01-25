"""
https://leetcode.com/problems/maximum-binary-tree/


654. Maximum Binary Tree
Medium

2102

252

Add to List

Share
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
Note:
The size of the given array will be in the range [1,1000].
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def f(nums):
            if not nums:
                return None
            j = 0
            for i in range(1, len(nums)):
                if nums[i] > nums[j]:
                    j = i
            root = TreeNode(nums[j])
            root.left = f(nums[:j])
            root.right = f(nums[j+1:])
            return root

        return f(nums)


if __name__ == '__main__':
    nums = [3,2,1,6,0,5]
    root = Solution().constructMaximumBinaryTree(nums)

    def inorder(root):
        if root:
            yield from inorder(root.left)
            yield root.val
            yield from inorder(root.right)

    for a, b in zip(inorder(root), nums):
        print(a, b)
        assert a == b

