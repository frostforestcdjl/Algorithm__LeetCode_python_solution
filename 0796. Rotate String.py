#Runtime: 20 ms, faster than 98.89% of Python3 online submissions for Rotate String.
#Memory Usage: 13.9 MB, less than 98.79% of Python3 online submissions for Rotate String.

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if goal[0] not in s:
            return False
        index = []
        for i in range(len(s)):
            if s[i] == goal[0]:
                index.append(i)
        for i in index:
            p = s[i:] + s[:i]
            if p == goal:
                return True
        return False
