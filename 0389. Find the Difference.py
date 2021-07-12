#Runtime: 40 ms, faster than 33.36% of Python3 online submissions for Find the Difference.
#Memory Usage: 14.2 MB, less than 84.17% of Python3 online submissions for Find the Difference.

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if set(t).difference(set(s)) != set():
            return list(set(t).difference(set(s)))[0]
        list_t = list(t)
        for i in s:
            list_t.remove(i)
        return list_t[0]
