#Runtime: 28 ms, faster than 92.68% of Python3 online submissions for Buddy Strings.
#Memory Usage: 14.1 MB, less than 99.77% of Python3 online submissions for Buddy Strings.

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) == len(goal):
            cand = []
            for i in range(len(s)):
                if s[i] != goal[i]:
                    cand.append([s[i], goal[i]])
                if len(cand) > 2:
                    return False
            if len(cand) == 0:
                for i in s:
                    if s.count(i) >= 2:
                        return True
            if len(cand) == 2:
                return cand[0][0] == cand[1][1] and cand[0][1] == cand[1][0]
        return False
