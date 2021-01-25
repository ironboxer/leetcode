/*

https://leetcode.com/problems/flatten-nested-list-iterator/


Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,1,2,1,1].
Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false,
             the order of elements returned by next should be: [1,4,6].

*/


package main


import "fmt"


/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * type NestedInteger struct {
 * }
 *
 * // Return true if this NestedInteger holds a single integer, rather than a nested list.
 * func (this NestedInteger) IsInteger() bool {}
 *
 * // Return the single integer that this NestedInteger holds, if it holds a single integer
 * // The result is undefined if this NestedInteger holds a nested list
 * // So before calling this method, you should have a check
 * func (this NestedInteger) GetInteger() int {}
 *
 * // Set this NestedInteger to hold a single integer.
 * func (n *NestedInteger) SetInteger(value int) {}
 *
 * // Set this NestedInteger to hold a nested list and adds a nested integer to it.
 * func (this *NestedInteger) Add(elem NestedInteger) {}
 *
 * // Return the nested list that this NestedInteger holds, if it holds a nested list
 * // The list length is zero if this NestedInteger holds a single integer
 * // You can access NestedInteger's List element directly if you want to modify it
 * func (this NestedInteger) GetList() []*NestedInteger {}
 */


type NestedIterator struct {
    Array []int   
    Pos int
}

func Constructor(nestedList []*NestedInteger) *NestedIterator {
    array := make([]int, 0) 
    var f func(p *NestedInteger)
    f = func(p *NestedInteger) {
        if p.IsInteger() {
            array = append(array, p.GetInteger())
        } else {
            list := p.GetList()
            for i := 0; i < len(list); i++ {
                f(list[i])
            }
        }
    }
    for i := 0; i < len(nestedList); i++ {
        f(nestedList[i])
    }
    obj := &NestedIterator{array, 0}
    return obj
}


func (this *NestedIterator) Next() int {
    val := this.Array[this.Pos]
    this.Pos++
    return val
}

func (this *NestedIterator) HasNext() bool {
    return this.Pos < len(this.Array) 
}


func main() {

}
