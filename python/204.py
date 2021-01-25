"""
https://leetcode.com/problems/count-primes/

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

"""


class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        i = 2
        while i ** 2 < n:
            j = 2
            while i * j < n:
                primes[i * j] = False
                j += 1
            i += 1
        return primes.count(True)



# 这个是效率最高的
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False

        for i in range(2, n):
            k = i ** 2
            if k >= n:
                break
            if not primes[k]:
                continue
            for j in range(k, n, i):
                primes[j] = False

        return primes.count(True)


if __name__ == '__main__':
    for i in range(2, 100):
        print(i, Solution().countPrimes(i))

