class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        power = []
        asc_pre = ''
        q = columnNumber
        while (q > 26):
            r = q%26
            if r == 0:
                r += 26
            power.append(r)
            q = int((q - r)/26)
        power.append(q)
        
        for i in range(len(power)):
            asc_pre = asc_pre + chr(power[-(i+1)]+64)
            
        return asc_pre
