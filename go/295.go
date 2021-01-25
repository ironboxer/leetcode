/*

https://leetcode.com/problems/find-median-from-data-stream/

Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

For example,
[2,3,4], the median is 3

[2,3], the median is (2 + 3) / 2 = 2.5

Design a data structure that supports the following two operations:

void addNum(int num) - Add a integer number from the data stream to the data structure.
double findMedian() - Return the median of all elements so far.


Example:

addNum(1)
addNum(2)
findMedian() -> 1.5
addNum(3)
findMedian() -> 2


Follow up:

If all integer numbers from the stream are between 0 and 100, how would you optimize it?
If 99% of all integer numbers from the stream are between 0 and 100, how would you optimize it?

*/


// 要实现这个算法需要一个高级一点的数据结构 叫做二叉堆 也叫做优先队列
// 但是golang是一种比较低层次的语言 没有如此高级的数据结构啊
package main


import "fmt"


type MedianFinder struct {

}


/** initialize your data structure here. */
func Constructor() MedianFinder {

}


func (this *MedianFinder) AddNum(num int)  {

}


func (this *MedianFinder) FindMedian() float64 {

}


/**
 * Your MedianFinder object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddNum(num);
 * param_2 := obj.FindMedian();
 */


func main() {

}
