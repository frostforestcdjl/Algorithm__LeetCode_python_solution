#Runtime: 144 ms, faster than 99.33% of Python3 online submissions for Assign Cookies.
#Memory Usage: 15.8 MB, less than 90.50% of Python3 online submissions for Assign Cookies.

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        c_n = 0
        g.sort(reverse=True)
        s.sort()
        for i in range(len(g)):
            if len(s) == 0: return c_n
            if g[i] <= s[-1]:
                c_n += 1
                s.pop(-1)
        return c_n
