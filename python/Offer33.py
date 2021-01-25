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


