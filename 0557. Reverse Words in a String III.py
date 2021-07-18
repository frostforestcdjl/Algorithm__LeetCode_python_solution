#Runtime: 88 ms, faster than 13.45% of Python3 online submissions for Reverse Words in a String III.
#Memory Usage: 14.8 MB, less than 73.23% of Python3 online submissions for Reverse Words in a String III.

class Solution:
    def reverseWords(self, s: str) -> str:
        r_s = ''
        while s.count(' ') > 0:
            r_s = r_s + s[s.index(' ')::-1]
            s = s[s.index(' ') + 1:]
        r_s += ' ' + s[::-1]
        return r_s[1:]
