package main

import "fmt"

type Item interface{}
type Stack struct {
	items []Item
}

func (this *Stack) Push(item Item) {
	this.items = append(this.items, item)
}

func (this *Stack) Pop() Item {
	last := len(this.items) - 1
	val := this.items[last]
	this.items = this.items[:last]
	return val
}

func (this *Stack) Len() int {
	return len(this.items)
}

func (this *Stack) Empty() bool {
	return this.Len() == 0
}

func (this *Stack) Peek() Item {
	return this.items[len(this.items)-1]
}

func main() {
	var stack Stack = Stack{}
	for i := 0; i < 10; i++ {
		stack.Push(i)
	}
	for !stack.Empty() {
		fmt.Println(stack.Peek(), stack.Pop())
	}
}
