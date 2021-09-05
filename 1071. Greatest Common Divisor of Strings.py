#Runtime: 28 ms, faster than 87.91% of Python3 online submissions for Greatest Common Divisor of Strings.
#Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Greatest Common Divisor of Strings.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        s1, s2 = len(str1), len(str2)
        while s1 != s2:
            if s2 > s1:
                s2 -= s1
            if s1 > s2:
                s1 -= s2
        return str1[:s1]


#Runtime: 32 ms, faster than 71.39% of Python3 online submissions for Greatest Common Divisor of Strings.
#Memory Usage: 14.2 MB, less than 58.34% of Python3 online submissions for Greatest Common Divisor of Strings.

class Solution2:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str2) > len(str1):
            str1, str2 = str2, str1
        while str1 and str2:
            try:
                if str1.index(str2) == 0:
                    str1 = str1.replace(str2, '')
                else:
                    return ''
                if str2.index(str1) == 0:
                    str2 = str2.replace(str1, '')
                else:
                    return ''
            except:
                return ''
        return max(str1, str2)
