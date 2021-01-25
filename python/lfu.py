from collections import defaultdict, Counter, deque


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.key_val = {}
        self.key_freq = Counter()
        # 这里用deque的原因是 每次pop的时候都把最早插入的元素pop掉
        self.freq_keys = defaultdict(deque)
        self.min_freq = 0

    def put(self, key, value):
        # 初始化一个容量为0的cache意义不大
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

    def get(self, key):
        val = self.key_val.get(key)
        if val is None:
            return -1
        self.increase_freq(key)
        return val

    def increase_freq(self, key):
        freq = self.key_freq[key]
        self.key_freq[key] += 1
        # NOTE: O(N)
        # 这个地方可以用OrderedDict优化
        # remove(key)的时间复杂度为O(n)
        self.freq_keys[freq].remove(key)
        self.freq_keys[freq + 1].append(key)
        # delete empty slot
        if not self.freq_keys[freq]:
            self.freq_keys.pop(freq)
            if freq == self.min_freq:
                self.min_freq += 1

    def remove_min_freq_key(self):
        key = self.freq_keys[self.min_freq].popleft()
        self.key_val.pop(key)
        self.key_freq.pop(key)


if __name__ == '__main__':
    lfu = LFUCache(10)
    for i in range(10):
        lfu.put(i, i)
        print(lfu.get(i))

    for i in range(10, 20):
        lfu.put(i, i)
        print(lfu.get(i-10), lfu.get(i))


    for i in range(100, 100000):
        lfu.put(i, i)

    print(lfu.get(99999))
    print(lfu.get(0))

