package main

import "fmt"


type T interface{}

type Deque struct {
    Items []T 
}


func Constructor() Deque {
    items := make([]T, 0)
    return Deque{Items: items}
}


func (this *Deque) Len() int {
    return len(this.Items)
}


func (this *Deque) Empty() bool {
    return this.Len() == 0
}


func (this *Deque) Append(item T) int {
    this.Items = append(this.Items, item)
    return this.Len()
}


func (this *Deque) PopLeft() T {
    val := this.Items[0]
    this.Items = this.Items[1:]
    return val
}


func (this *Deque) PopRight() T {
    total := this.Len()
    val := this.Items[total - 1]
    this.Items = this.Items[:total - 1]
    return val
}


func main() {
    queue := Constructor()
    for i := 0; i < 10; i++ {
        t := queue.Append(i)
        fmt.Println(t)
    }

    fmt.Println(queue.Len())

    for !queue.Empty() {
        fmt.Println(queue.PopLeft())
    }

    for i := 0; i < 10; i++ {
        t := queue.Append(i)
        fmt.Println(t)
    }

    fmt.Println(queue.Len())

    for !queue.Empty() {
        fmt.Println(queue.PopRight())
    }
}

