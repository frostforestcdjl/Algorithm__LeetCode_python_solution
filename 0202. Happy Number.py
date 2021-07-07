class Solution:
    def isHappy(self, n: int) -> bool:
        s = list(str(n))
        temp_sq = 0
        repead_check = []
        while s != ['1']:
            for i in range(len(s)):
                temp_sq += int(s[i])**2
            s = list(str(temp_sq))
            try:
                repead_check.index(s)
                return False
            except:
                pass
            repead_check.append(s)
            temp_sq = 0
        return True
