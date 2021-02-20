"""
https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/description/


剑指 Offer 59 - II. 队列的最大值
请定义一个队列并实现函数 max_value 得到队列里的最大值，要求函数max_value、push_back 和 pop_front 的均摊时间复杂度都是O(1)。

若队列为空，pop_front 和 max_value 需要返回 -1

示例 1：

输入:
["MaxQueue","push_back","push_back","max_value","pop_front","max_value"]
[[],[1],[2],[],[],[]]
输出: [null,null,null,2,1,2]
示例 2：

输入:
["MaxQueue","pop_front","max_value"]
[[],[],[]]
输出: [null,-1,-1]


限制：

1 <= push_back,pop_front,max_value的总操作数 <= 10000
1 <= value <= 10^5
"""


from collections import deque


class MaxQueue:


    """
    试想两种情况 12345 54321
    12345 只保留 5
    而54321 则保留 54321
    因为如果最早的5弹出之后 4 变为最大的元素了
    所以deque保存的是一个降序的序列 也可能存在重复的
    比如 55555 则deque中保存的就是55555
    对于deque因为每个元素最多入队列 出队列一次
    所以平摊时间复杂度就是O(1)
    """

    def __init__(self):
        self.deque = deque()
        self.queue = deque()

    def max_value(self) -> int:
        return self.deque[-1] if self.deque else -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.append(value)

    def pop_front(self) -> int:
        if not self.queue:
            return -1
        val = self.queue.popleft()
        if val == self.deque[0]:
            self.deque.popleft()
        return val


# Your MaxQueue object will be instantiated and called as such:
# obj = MaxQueue()
# param_1 = obj.max_value()
# obj.push_back(value)
# param_3 = obj.pop_front()
