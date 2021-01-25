"""

"""


from threading import Thread, Semaphore


def printNumber(x):
    print(x, end='')


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.s1 = Semaphore(1)
        self.s2 = Semaphore(0)
        self.s3 = Semaphore(0)

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(self.n):
            self.s1.acquire()
            printNumber(0)
            self.s2.release()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.s2.acquire()
            if not i & 1:
                printNumber(i)
            self.s3.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n + 1):
            self.s3.acquire()
            if i & 1:
                printNumber(i)
            self.s1.release()


if __name__ == '__main__':
    n = 5
    z = ZeroEvenOdd(n)

    t1 = Thread(target=z.zero, args=(printNumber, ))
    t2 = Thread(target=z.even, args=(printNumber, ))
    t3 = Thread(target=z.odd,  args=(printNumber, ))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

