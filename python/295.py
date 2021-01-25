"""
https://leetcode.com/problems/find-median-from-data-stream/

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

"""

# 算是非常经典的一个算法


from heapq import heappush, heappushpop, heappop

class MedianFinder:
    """
    构建两个二叉堆
    一个最大堆
    一个最小堆
    最小堆的堆顶元素大于最大堆的堆顶元素
    从而保证最小堆的整体元素都大于最大堆的全部元素
    从而把寻找中间元素的操作 抽象为 两个堆 堆顶元素的操作
    """

    def __init__(self):
        self.A = []
        self.B = []

    def addNum(self, num: int) -> None:
        x = heappushpop(self.B, num)
        # x  是最小的的最小的元素
        heappush(self.A, -x)
        # 保证最小堆中的元素数量>=最大堆中的元素数量
        if len(self.A) > len(self.B):
            y = heappop(self.A)
            heappush(self.B, -y)
        print(self.A, self.B)


    def findMedian(self) -> float:
        """
        默认最小堆中的元素数量>=最大堆中的元素数量
        """
        if len(self.A) == len(self.B):
            return (self.B[0] - self.A[0]) / 2
        return self.B[0]


from heapq import heappush, heappop, heappushpop

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.S, self.L = [], []

    def addNum(self, num: int) -> None:
        x = heappushpop(self.L, num)
        heappush(self.S, -x)
        if len(self.S) > len(self.L):
            y = heappop(self.S)
            heappush(self.L, -y)

    def findMedian(self) -> float:
        if len(self.S) == len(self.L):
            return (self.L[0] - self.S[0]) / 2
        return self.L[0]


# 如此标准的操作



if __name__ == '__main__':
    s = MedianFinder()
    for i in range(10):
        s.addNum(i)
        print([j for j in range(i+1)], s.findMedian())

