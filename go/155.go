/*

https://leetcode.com/problems/min-stack/

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.


Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

Methods pop, top and getMin operations will always be called on non-empty stacks.

*/


package main


import "fmt"


type MinStack struct {
    Stack [][2]int
}


/** initialize your data structure here. */
func Constructor() MinStack {
    stack := make([][2]int, 0)
    obj := MinStack{Stack: stack}
    return obj
}


func (this *MinStack) Push(x int)  {
    if len(this.Stack) == 0 {
        this.Stack = append(this.Stack, [2]int{x, x})
    } else {
        y := this.Stack[len(this.Stack) - 1][1]
        if x < y  {
            y = x
        }
        this.Stack = append(this.Stack, [2]int{x, y})
    }
}


func (this *MinStack) Pop()  {
    this.Stack = this.Stack[:len(this.Stack) - 1]
}


func (this *MinStack) Top() int {
    r := this.Stack[len(this.Stack) - 1]
    return r[0]
}


func (this *MinStack) GetMin() int {
    r := this.Stack[len(this.Stack) - 1]
    return r[1]
}


func main() {
    stack := Constructor()
    stack.Push(-2)
    stack.Push(0)
    stack.Push(-3)
    fmt.Println(stack.GetMin())
    stack.Pop()
    fmt.Println(stack.Top())
    fmt.Println(stack.GetMin()) 
}
