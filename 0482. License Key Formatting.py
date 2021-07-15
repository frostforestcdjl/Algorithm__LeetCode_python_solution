#Runtime: 176 ms, faster than 11.85% of Python3 online submissions for License Key Formatting.
#Memory Usage: 14.5 MB, less than 99.45% of Python3 online submissions for License Key Formatting.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.upper()
        s = s + '='
        i = 2
        check = True
        while check:
            try:
                while s[-i] == '-' and (i-1)%(k+1) != 0:
                    s = s[:-i] + s[-i+1:]
                if (i-1)%(k+1) == 0 and s[-i] != '-':
                    s = s[:-i+1] + '-' + s[-i+1:]
                i += 1
            except:
                check = False
        if s[0] == '-':
            s = s[1:]
        return s[:-1]
            
