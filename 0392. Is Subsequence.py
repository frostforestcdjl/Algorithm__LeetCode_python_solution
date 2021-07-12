#Runtime: 24 ms, faster than 97.03% of Python3 online submissions for Is Subsequence.
#Memory Usage: 14.2 MB, less than 74.59% of Python3 online submissions for Is Subsequence.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in t:
            if len(s) == 0:
                return True
            if i == s[0]:
                    s = s[1:]
        if len(s) == 0:
                return True
        return False
