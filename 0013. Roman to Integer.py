#Runtime: 40 ms, faster than 93.42% of Python3 online submissions for Roman to Integer.
#Memory Usage: 13.9 MB, less than 99.35% of Python3 online submissions for Roman to Integer.

class Solution:
    def romanToInt(self, s: str) -> int:
        sum_r = 0
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        for i in range(len(s)-1):
            if dic[s[i]] < dic[s[i+1]]:
                sum_r -= dic[s[i]]
            else:
                sum_r += dic[s[i]]
        sum_r += dic[s[-1]]
        return sum_r
