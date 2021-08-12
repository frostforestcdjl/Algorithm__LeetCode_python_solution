#Runtime: 16 ms, faster than 99.92% of Python3 online submissions for Backspace String Compare.
#Memory Usage: 14.1 MB, less than 80.65% of Python3 online submissions for Backspace String Compare.

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        while '#' in s:
            if s.index('#') > 0:
                s = s[:s.index('#')-1] + s[s.index('#')+1:]
            else:
                s = s[1:]
        while '#' in t:
            if t.index('#') > 0:
                t = t[:t.index('#')-1] + t[t.index('#')+1:]
            else:
                t = t[1:]
        return s == t
