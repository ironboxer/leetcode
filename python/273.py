"""
https://leetcode.com/problems/integer-to-english-words/


Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"

Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"

"""


class Solution:

    def numberToWords(self, num: int) -> str:
        A =  ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        B = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

        def f(n):
            if n < 20:
                return A[n-1: n]
            if n < 100:
                return [A[n//10 - 2]] + f(n % 10)
            if n < 1000:
                return [B[n//100-1]] + ['Hundred'] + f(n % 100)
            for i, e in enumerate(('Thousand', 'Million', 'Billion'), 1):
                if n < 1000 ** (i + 1):
                    return f(n // (1000 ** i)) + [e] + f(n % (1000 ** i))

        return ' '.join(map(str, f(num))) or 'Zero'


if __name__ == '__main__':
    print(Solution().numberToWords(1234567891))

