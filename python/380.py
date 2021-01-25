"""
https://leetcode.com/problems/insert-delete-getrandom-o1/

Design a data structure that supports all following operations in average O(1) time.



insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.


Example:

// Init an empty set.
RandomizedSet randomSet = new RandomizedSet();

// Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomSet.insert(1);

// Returns false as 2 does not exist in the set.
randomSet.remove(2);

// Inserts 2 to the set, returns true. Set now contains [1,2].
randomSet.insert(2);

// getRandom should return either 1 or 2 randomly.
randomSet.getRandom();

// Removes 1 from the set, returns true. Set now contains [2].
randomSet.remove(1);

// 2 was already in the set, so return false.
randomSet.insert(2);

// Since 2 is the only number in the set, getRandom always return 2.
randomSet.getRandom();
"""


import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.index = []
        self.memo = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        pos = self.memo.get(val)
        if pos is not None:
            return False
        self.index.append(val)
        self.memo[val] = len(self.index) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        pos = self.memo.get(val)
        if pos is None:
            return False
        if pos + 1 == len(self.index):
            self.index.pop()
            self.memo.pop(val)
        else:
            self.index[pos], self.index[-1] = self.index[-1], self.index[pos]
            self.memo[self.index[pos]] = pos
            self.index.pop()
            self.memo.pop(val)
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return random.choice(self.index)

# 仔细体会字典和数组的使用
# 和python3中的字典实现有什么异同?


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

