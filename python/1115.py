"""
https://leetcode-cn.com/problems/print-foobar-alternately/


1115. 交替打印FooBar
我们提供一个类：

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
两个不同的线程将会共用一个 FooBar 实例。其中一个线程将会调用 foo() 方法，另一个线程将会调用 bar() 方法。

请设计修改程序，以确保 "foobar" 被输出 n 次。



示例 1:

输入: n = 1
输出: "foobar"
解释: 这里有两个线程被异步启动。其中一个调用 foo() 方法, 另一个调用 bar() 方法，"foobar" 将被输出一次。
示例 2:

输入: n = 2
输出: "foobarfoobar"
解释: "foobar" 将被输出两次。
"""


def printFoo():
    print('foo', end='')


def printBar():
    print('bar', end='')


import queue
from threading import Thread


class FooBar:
    def __init__(self, n):
        self.n = n
        self.queue = queue.Queue(maxsize=1)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.queue.put(1)
            printFoo()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.queue.get()
            printBar()


from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.A = Semaphore(1)
        self.B = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:

        for i in range(self.n):
            self.A.acquire()
            printFoo()
            self.B.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.B.acquire()
            printBar()
            self.A.release()

# Good


if __name__ == '__main__':
    fb = FooBar(3)
    f = Thread(target=fb.foo, name='foo', args=(printFoo,))
    b = Thread(target=fb.bar, name='bar', args=(printBar,))
    f.start()
    b.start()
    f.join()
    b.join()

