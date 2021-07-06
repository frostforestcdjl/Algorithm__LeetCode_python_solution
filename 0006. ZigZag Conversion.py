class Solution:
    def convert(self, s: str, numRows: int) -> str:
        group_n = (numRows - 1)*2
        out_s = ''
        if group_n == 0:
            return s
        for i in range(numRows):
            for j in range(i, len(s)):
                if (j%group_n == i) or (j%group_n == (group_n - i)):
                    out_s += s[j]
                    
        return out_s
