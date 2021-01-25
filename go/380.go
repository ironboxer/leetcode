/*


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

*/


package main


import "fmt"
import "math/rand"



type RandomizedSet struct {
    Dict map[int]int
    List []int
}


/** Initialize your data structure here. */
func Constructor() RandomizedSet {
    dict := make(map[int]int)
    list := make([]int, 0)
    obj := RandomizedSet{dict, list}
    return obj
}


/** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
func (this *RandomizedSet) Insert(val int) bool {
    if _, ok := this.Dict[val]; ok {
        return false
    }
    pos := len(this.List)
    this.List = append(this.List, val)
    this.Dict[val] = pos
    return true
}


/** Removes a value from the set. Returns true if the set contained the specified element. */
func (this *RandomizedSet) Remove(val int) bool {
    pos, ok := this.Dict[val]
    if !ok {
        return false
    }
    // last one
    if pos + 1 == len(this.List) {
        this.List = this.List[:pos]
        delete(this.Dict, val)
    } else {
        last := len(this.List) - 1
        lastVal := this.List[last]
        this.Dict[lastVal] = pos
        this.List[pos], this.List[last] = this.List[last], this.List[pos]
        this.List = this.List[:last]
        delete(this.Dict, val)
    }
    return true
}


/** Get a random element from the set. */
func (this *RandomizedSet) GetRandom() int {
    n := rand.Int()
    pos := n % len(this.List)
    return this.List[pos]
}


func main() {
    randomizedSet := Constructor()
    randomizedSet.Insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
    randomizedSet.Remove(2); // Returns false as 2 does not exist in the set.
    randomizedSet.Insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
    fmt.Println(randomizedSet.GetRandom()); // getRandom() should return either 1 or 2 randomly.
    randomizedSet.Remove(1); // Removes 1 from the set, returns true. Set now contains [2].
    randomizedSet.Insert(2); // 2 was already in the set, so return false.
    fmt.Println(randomizedSet.GetRandom()); // Since 2 is the only number in the set, getRandom() will always return 2.
}
