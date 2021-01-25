"""
https://leetcode.com/problems/lru-cache/

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
Follow up:
Could you do get and put in O(1) time complexity?

 

Example 1:

Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]

Explanation
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
 

Constraints:

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
At most 3 * 104 calls will be made to get and put.

"""


class Node:
    def __init__(self, key=None, val=None, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

    def __str__(self):
        return f'{self.key}:{self.val}:prev:next'

    def __repr__(self):
        return str(self)


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.top = Node()
        self.tail = Node()
        self.tail.next = self.top
        self.top.prev = self.tail

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            val = node.val
            self._delete(node)
            self._insert(key, val)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._delete(self.cache[key])
        if len(self.cache) == self.cap:
            self._delete(self.tail.next)
        self._insert(key, value)

    def _delete(self, node):
        self.cache.pop(node.key)
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert(self, key, val):
        node = Node(key=key, val=val)
        node.prev = self.top.prev
        self.top.prev.next = node
        node.next = self.top
        self.top.prev = node
        self.cache[key] = node


# 新增dummy节点的好处就是没有了 if else 判断 top tail 节点是否为空的逻辑, 整体上非常统一了

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


if __name__ == '__main__':
    cache = LRUCache(2)

    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)

    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)
