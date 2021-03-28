"""
https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/

剑指 Offer 33. 二叉搜索树的后序遍历序列
输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。如果是则返回 true，否则返回 false。假设输入的数组的任意两个数字都互不相同。



参考以下这颗二叉搜索树：

     5
    / \
   2   6
  / \
 1   3
示例 1：

输入: [1,6,3,2,5]
输出: false
示例 2：

输入: [1,3,2,6,5]
输出: true


提示：

数组长度 <= 1000
"""


from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:

        def f(postorder):
            print(postorder)
            total = len(postorder)
            if total < 2:
                return True

            top = postorder[total-1]
            i = 0
            while i < total - 1:
                if postorder[i] > top:
                    break
                i += 1
            for j in range(i, total - 1):
                if postorder[j] < top:
                    return False

            return f(postorder[:i]) and f(postorder[i:total-1])

        return f(postorder)


class Solution:
    """
    利用二叉搜索树的性质 以及后序遍历的性质
    比如
           2
        1     3
    根据二叉搜索树的后序遍历 结果应该是 1 3 2
    解题思路就是从后面每次都弹出一个元素 作为父节点的元素
    那么应该可以将序列划分为两部分：左侧部署小于父节点 右侧部署大于父节点
    这就是基本的思路
    如果发现左侧为空或者是右侧为空的情况 则是当前节点不是父节点 而是 一个 左节点 或者 右节点
    基本的思路就是这样
    """
    def verifyPostorder(self, postorder: List[int]) -> bool:
        while postorder:
            n = postorder.pop()
            i = 0
            while i < len(postorder) and postorder[i] < n:
                i += 1
            while i < len(postorder) and postorder[i] > n:
                i += 1
            if i < len(postorder):
                return False
        return True


if __name__ == '__main__':
    nodes = [1,6,3,2,5]
    print(nodes)
    print(Solution().verifyPostorder(nodes))

    nodes = [1,3,2,6,5]
    print(nodes)
    print(Solution().verifyPostorder(nodes))

    nodes = [4, 8, 6, 12, 16, 14, 10]
    print(nodes)
    print(Solution().verifyPostorder(nodes))


