#Runtime: 28 ms, faster than 78.88% of Python3 online submissions for Number of Segments in a String.
#Memory Usage: 13.9 MB, less than 97.52% of Python3 online submissions for Number of Segments in a String.

class Solution:
    def countSegments(self, s: str) -> int:
        if len(s) == 0:
            return 0
        wd = 0
        for i in range(len(s) - 1):
            if (s[i] != ' ') and (s[i+1] == ' '):
                wd += 1
        if s[-1] != ' ':
            wd += 1
        return wd
