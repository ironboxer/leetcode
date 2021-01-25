class Node:
    def __init__(self, key, val, prev=None, next_=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next_

    def __str__(self):
        return f'<%d:%d>' % (self.key, self.val)

    def __repr__(self):
        return str(self)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        # head tail 的使用非常关键
        # 化简了很多指针判空的操作
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if node is None:
            return -1

        retval = node.val

        prev, next_ = node.prev, node.next
        prev.next, next_.prev = next_, prev

        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

        return retval

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.val = value
        else:
            node = Node(key, value)
            self.cache[key] = node

        prev, next_ = node.prev, node.next
        if prev:
            prev.next = next_
        if next_:
            next_.prev = prev

        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

        if len(self.cache) > self.capacity:
            node = self.tail.prev
            prev = node.prev
            prev.next = self.tail
            self.tail.prev = prev

            node.prev = node.nexg = None

            self.cache.pop(node.key)


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1))

    cache.put(3, 3)
    print(cache.get(2))
    cache.put(4, 4)
    print(cache.get(1))
    print(cache.get(3))
    print(cache.get(4))

