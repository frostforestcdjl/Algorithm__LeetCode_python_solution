#Runtime: 1648 ms, faster than 6.69% of Python3 online submissions for Repeated Substring Pattern.
#Memory Usage: 14.1 MB, less than 94.64% of Python3 online submissions for Repeated Substring Pattern.

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2):
            if s.count(s[:i+1]) * (i+1) == len(s):
                return True
        return False
