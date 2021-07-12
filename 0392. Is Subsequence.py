#Runtime: 32 ms, faster than 70.88% of Python3 online submissions for Is Subsequence.
#Memory Usage: 14.2 MB, less than 74.59% of Python3 online submissions for Is Subsequence.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        for i in t:
            if i == s[0]:
                    s = s[1:]
            if len(s) == 0:
                return True
        return False 
