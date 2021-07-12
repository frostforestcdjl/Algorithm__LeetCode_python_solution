#Runtime: 4936 ms, faster than 5.13% of Python3 online submissions for First Unique Character in a String.
#Memory Usage: 14.1 MB, less than 99.51% of Python3 online submissions for First Unique Character in a String.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i in s:
            if s.count(i) == 1:
                return s.index(i)
        return -1
