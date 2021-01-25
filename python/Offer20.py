"""
https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/

剑指 Offer 20. 表示数值的字符串
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"-1E-16"、"0123"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。
"""

class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
        except ValueError:
            return False

        return True

# https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/java-dfafu-tu-by-zdxiq125/

class Solution:
    FSM = {
        0: {'s': 1, 'n': 2, 'd': 8},
        1: {'n': 2, 'd': 8},
        2: {'n': 2, 'd': 3, 'e': 5},
        3: {'n': 4, 'e': 5},
        4: {'n': 4, 'e': 5},
        5: {'s': 6, 'n': 7},
        6: {'n': 7},
        7: {'n': 7},
        8: {'n': 4},
    }
    END = {2, 3, 4, 7}

    def getType(self, c):
        if c in ('E', 'e'):
            return 'e'
        elif '0' <= c <= '9':
            return 'n'
        elif c in ('+', '-'):
            return 's'
        elif c == '.':
            return 'd'

        return '\0'

    def isNumber(self, s: str) -> bool:
        FSM, getType = self.FSM, self.getType

        s = s.strip()
        cur = 0
        for c in s:
            nxt = FSM[cur].get(getType(c), -1)
            if nxt < 0:
                return False
            cur = nxt

        return cur in self.END


if __name__ == '__main__':
    s = '2e+5.4'
    print(Solution().isNumber(s))

