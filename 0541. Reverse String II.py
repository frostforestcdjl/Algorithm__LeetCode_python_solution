#Runtime: 20 ms, faster than 99.67% of Python3 online submissions for Reverse String II.
#Memory Usage: 14.6 MB, less than 17.24% of Python3 online submissions for Reverse String II.

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        new_s = ''
        odd = True
        while len(s) > 0:
            if odd == True:
                new_s += s[k-1::-1]
                odd = False
            else:
                new_s += s[:k]
                odd = True
            s = s[k:]
        return new_s
