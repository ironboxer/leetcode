"""
https://leetcode-cn.com/problems/design-linked-list/

707. 设计链表
设计链表的实现。您可以选择使用单链表或双链表。单链表中的节点应该具有两个属性：val 和 next。val 是当前节点的值，next 是指向下一个节点的指针/引用。如果要使用双向链表，则还需要一个属性 prev 以指示链表中的上一个节点。假设链表中的所有节点都是 0-index 的。

在链表类中实现这些功能：

get(index)：获取链表中第 index 个节点的值。如果索引无效，则返回-1。
addAtHead(val)：在链表的第一个元素之前添加一个值为 val 的节点。插入后，新节点将成为链表的第一个节点。
addAtTail(val)：将值为 val 的节点追加到链表的最后一个元素。
addAtIndex(index,val)：在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
deleteAtIndex(index)：如果索引 index 有效，则删除链表中的第 index 个节点。


示例：

MyLinkedList linkedList = new MyLinkedList();
linkedList.addAtHead(1);
linkedList.addAtTail(3);
linkedList.addAtIndex(1,2);   //链表变为1-> 2-> 3
linkedList.get(1);            //返回2
linkedList.deleteAtIndex(1);  //现在链表是1-> 3
linkedList.get(1);            //返回3


提示：

所有val值都在 [1, 1000] 之内。
操作次数将在  [1, 1000] 之内。
请不要使用内置的 LinkedList 库。

"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None


def visit(node):
    while node:
        print(node.val, end=',')
        node = node.next
    print()


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        cur = self.head
        for _ in range(index):
            if cur.next is self.tail:
                return -1
            cur = cur.next
        # visit(self.head.next)
        return cur.next.val

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        new_node = ListNode(val)
        prev = self.head
        nxt = self.head.next

        nxt.prev = new_node
        new_node.next = nxt

        prev.next = new_node
        new_node.prev = prev
        # visit(self.head.next)

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        new_node = ListNode(val)
        prev = self.tail.prev
        nxt = self.tail

        prev.next = new_node
        new_node.prev = prev

        nxt.prev = new_node
        new_node.next = nxt
        # visit(self.head.next)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        cur = self.head
        for i in range(index):
            if cur.next is self.tail:
                return
            cur = cur.next

        new_node = ListNode(val)
        prev = cur
        nxt = cur.next

        prev.next = new_node
        new_node.prev = prev

        nxt.prev = new_node
        new_node.next = nxt
        # visit(self.head.next)

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        cur = self.head
        for i in range(index):
            if cur.next is self.tail:
                return
            cur = cur.next
        # 补丁
        if cur.next is self.tail:
            return
        delete_node = cur.next
        prev = cur
        nxt = delete_node.next

        prev.next = nxt
        nxt.prev = prev

        delete_node.prev = delete_node.next = None
        # visit(self.head.next)


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
