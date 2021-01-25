"""
https://leetcode.com/problems/h-index/

Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had
             received 3, 0, 6, 1, 5 citations respectively.
             Since the researcher has 3 papers with at least 3 citations each and the remaining
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.

"""


from typing import List


class Solution:
    """
    论文引用的定义
    被引用的数量 >= 论文的总数量
    """
    def hIndex(self, citations: List[int]) -> int:
        A = sorted(citations)
        while A and A[0] < len(A):
            A = A[1:]
        return len(A)


class Solution:
    """
    桶排序
    这里的bucket, 其实相当于一中normalization
    couting sort ? alias bucket sort
    """
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        buckets = [0] * (n + 1)
        for i in citations:
            if i >= n:
                buckets[n] += 1
            else:
                buckets[i] += 1
        # buckets 记录的是出现的次数
        print(buckets)
        res = 0
        for i in range(n, -1, -1):
            res += buckets[i]
            if res >= i:
                return i
        return 0


if __name__ == '__main__':
    print(Solution().hIndex([100, 100, 100]))
    print(Solution().hIndex([3, 0, 6, 1, 5]))

