"""
https://leetcode-cn.com/problems/lfu-cache/


460. LFU 缓存
请你为 最不经常使用（LFU）缓存算法设计并实现数据结构。

实现 LFUCache 类：

LFUCache(int capacity) - 用数据结构的容量 capacity 初始化对象
int get(int key) - 如果键存在于缓存中，则获取键的值，否则返回 -1。
void put(int key, int value) - 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除 最久未使用 的键。
注意「项的使用次数」就是自插入该项以来对其调用 get 和 put 函数的次数之和。使用次数会在对应项被移除后置为 0 。



进阶：

你是否可以在 O(1) 时间复杂度内执行两项操作？


示例：

输入：
["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
输出：
[null, null, null, 1, null, -1, 3, null, -1, 3, 4]

解释：
LFUCache lFUCache = new LFUCache(2);
lFUCache.put(1, 1);
lFUCache.put(2, 2);
lFUCache.get(1);      // 返回 1
lFUCache.put(3, 3);   // 去除键 2
lFUCache.get(2);      // 返回 -1（未找到）
lFUCache.get(3);      // 返回 3
lFUCache.put(4, 4);   // 去除键 1
lFUCache.get(1);      // 返回 -1（未找到）
lFUCache.get(3);      // 返回 3
lFUCache.get(4);      // 返回 4


提示：

0 <= capacity, key, value <= 104
最多调用 105 次 get 和 put 方法
"""


from collections import Counter, defaultdict


class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_val = {}
        self.key_freq = Counter()
        self.freq_keys = defaultdict(deque)
        self.min_freq = 0

    def get(self, key: int) -> int:
        val = self.key_val.get(key)
        if val is None:
            return -1
        # increase key frequency
        self.increase_freq(key)
        return val


    def put(self, key: int, value: int) -> None:
        # no space
        if self.capacity <= 0:
            return

        if key in self.key_val:
            self.key_val[key] = value
            self.increase_freq(key)
            return

        if self.capacity <= len(self.key_val):
            self.remove_min_freq_key()

        self.key_val[key] = value
        self.key_freq[key] = 1
        self.freq_keys[1].append(key)
        self.min_freq = 1

    def increase_freq(self, key):
        freq = self.key_freq[key]
        self.key_freq[key] += 1
        self.freq_keys[freq].remove(key)
        self.freq_keys[freq + 1].append(key)
        if not self.freq_keys[freq]:
            self.freq_keys.pop(freq)
            if freq == self.min_freq:
                self.min_freq += 1

    def remove_min_freq_key(self):
        key = self.freq_keys[self.min_freq].popleft()
        self.key_val.pop(key)
        self.key_freq.pop(key)


