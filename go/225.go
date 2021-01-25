/*

https://leetcode.com/problems/implement-stack-using-queues/

Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.
Example:

MyStack stack = new MyStack();

stack.push(1);
stack.push(2);
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

*/


package main


import "fmt"


type MyStack struct {
    List []int
}


/** Initialize your data structure here. */
func Constructor() MyStack {
    list := make([]int, 0)
    obj := MyStack{list}
    return obj
}


/** Push element x onto stack. */
func (this *MyStack) Push(x int)  {
    this.List = append(this.List, x)
}


/** Removes the element on top of the stack and returns that element. */
func (this *MyStack) Pop() int {
    x := this.List[len(this.List) - 1]
    this.List = this.List[:len(this.List) - 1]
    return x
}


/** Get the top element. */
func (this *MyStack) Top() int {
    x := this.List[len(this.List) - 1]
    return x
}


/** Returns whether the stack is empty. */
func (this *MyStack) Empty() bool {
    return len(this.List) == 0
}


// SB代码

func main() {

}
