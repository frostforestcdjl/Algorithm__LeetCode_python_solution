#Runtime: 3232 ms, faster than 5.06% of Python3 online submissions for Assign Cookies.
#Memory Usage: 15.8 MB, less than 82.95% of Python3 online submissions for Assign Cookies.

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c_n = 0
        g.sort(reverse=True)
        for i in range(len(g)):
            if len(s) == 0:
                break
            if g[i] <= max(s):
                c_n += 1
                s.remove(max(s))
        return c_n
