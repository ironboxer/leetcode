"""
https://leetcode-cn.com/problems/restore-ip-addresses/

93. 复原IP地址
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

有效的 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效的 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效的 IP 地址。



示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "1111"
输出：["1.1.1.1"]
示例 4：

输入：s = "010010"
输出：["0.10.0.10","0.100.1.0"]
示例 5：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


提示：

0 <= s.length <= 3000
s 仅由数字组成
"""

def check(text):
    try:
        assert 1 <= len(text) <= 3 and 0 <= int(text) <= 255
    except:
        return False
    else:
        if len(text) > 1:
            return text[0] != '0'
        return True


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def f(s, buf):
            if len(buf) == 3:
                if check(s):
                    buf.append(s)
                    res.append(".".join(buf))
                    buf.pop()
                return
            for i in range(len(s)-1):
                if check(s[:i+1]):
                    buf.append(s[:i+1])
                    f(s[i+1:], buf)
                    buf.pop()

        f(s, [])
        return res




# 做1万遍都不会
def check(s):
    if not (1 <= len(s) <= 3 and 0 <= int(s) <= 255):
        return False
    if len(s) > 1 and s[0] == '0':
        return False
    return True


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def f(s, buf):
            if len(buf) == 3:
                if check(s):
                    buf.append(s)
                    res.append('.'.join(buf))
                    buf.pop()
                return
            for i in range(len(s)):
                if check(s[:i+1]):
                    buf.append(s[:i+1])
                    f(s[i+1:], buf)
                    buf.pop()

        f(s, [])

        return res


