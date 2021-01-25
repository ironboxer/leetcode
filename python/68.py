"""
https://leetcode.com/problems/text-justification/


Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.
Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.
Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]
"""

from typing import List


class Solution1:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res, cur, num = [], [], 0
        for w in words:
            if num + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num = [], 0
            cur += [w]
            num += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        buf = []
        for word in words:
            if len(buf) + sum(len(w) for w in buf) + len(word) > maxWidth:
                if len(buf) == 1:
                    res.append(buf[0] + ' ' * (maxWidth - len(buf[0])))
                else:
                    sep, pad = divmod(maxWidth - sum(len(w) for w in buf), len(buf) - 1)
                    for i in range(pad):
                        buf[i] += ' '
                    res.append((' ' * sep).join(buf))

                buf = [word]
            else:
                buf.append(word)

        if buf:
            if len(buf) == 1:
                res.append(buf[0] + ' ' * (maxWidth - len(buf[0])))
            else:
                pad = ' ' * (maxWidth - sum(len(w) for w in buf) - len(buf))
                if pad:
                    buf.append(pad)
                res.append(' '.join(buf))

        return res


# 终于过了, 很不容易啊, 能把很多case统一起来处理,的算法才是最好的

if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    r = Solution().fullJustify(words, 16)
    for l in r:
        print(l, len(l))
    print('\n')

    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    r = Solution().fullJustify(words, 16)
    for l in r:
        print(l, len(l))
    print('\n')

    words = ["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do",
             "for",
             "your", "country"]
    r = Solution().fullJustify(words, 16)
    for l in r:
        print(l, len(l))
    print('\n')

    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    r = Solution().fullJustify(words, 16)
    for l in r:
        print(l, len(l))
    print('\n')

    words = ["ask", "not", "what", "your", "country", "can", "do", "for", "you", "ask", "what", "you", "can", "do",
             "for", "your", "country"]
    r = Solution().fullJustify(words, 16)
    for l in r:
        print(l, len(l))
    print('\n')
