/*

https://leetcode.com/problems/lru-cache/description/

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

*/


package main


import "fmt"


// 下面这个方法非常的巧妙
// 这道题必须使用链表 不需要使用数组
// 因为前后的关系是相对的 


type Node struct {
    Key int
    Val int
    Prev *Node
    Next *Node
}


type LRUCache struct {
    Cap int
    Cache map[int]*Node
    // 指向最新插入的节点
    Top *Node
    // 指向最早插入的节点
    Tail *Node
}


func Constructor(capacity int) LRUCache {
    cache := make(map[int]*Node)
    top := &Node{-1, -1, nil, nil}
    tail := &Node{-1, -1, nil, nil}
    // 最早插入的节点的下一个节点是top
    // 最新插入的节点的前一个节点是tail
    // 这个设计是合理的
    tail.Next = top
    top.Prev = tail
    obj := LRUCache {
        Cap: capacity,
        Cache: cache,
        Top: top,
        Tail: tail,
    }
    return obj
}


// 这两个函数的思路都很简单
// 复杂的地方交给了deleteNode insertNode
func (this *LRUCache) Get(key int) int {
    node, ok := this.Cache[key]
    if !ok {
        return -1
    }
    val := node.Val
    this.deleteNode(node)
    this.insertNode(key, val)
    return val
}


func (this *LRUCache) Put(key int, value int)  {
    node, ok := this.Cache[key]
    if ok {
        this.deleteNode(node)
    }
    if len(this.Cache) == this.Cap {
        this.deleteNode(this.Tail.Next)
    }
    this.insertNode(key, value)
}


// 删除的逻辑十分的清晰
func (this *LRUCache) deleteNode(node *Node) {
    delete(this.Cache, node.Key)
    prevNode := node.Prev
    nextNode := node.Next
    prevNode.Next = nextNode
    nextNode.Prev = prevNode
}


// 插入的逻辑也很简单
func (this *LRUCache) insertNode(key int, value int) {
    node := &Node{
        Key: key,
        Val: value,
        Prev: nil,
        Next: nil,
    }
    node.Prev = this.Top.Prev
    this.Top.Prev.Next = node
    node.Next = this.Top
    this.Top.Prev = node
    this.Cache[key] = node
}



func main() {
    lruCache := Constructor(2)
    lruCache.Put(1, 1)
    lruCache.Put(2, 2)
    fmt.Println(lruCache.Get(1))
    lruCache.Put(3, 3)
    fmt.Println(lruCache.Get(2))
    lruCache.Put(4, 4)
    fmt.Println(lruCache.Get(1))
    fmt.Println(lruCache.Get(3))
    fmt.Println(lruCache.Get(4))
}
