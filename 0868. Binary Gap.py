#Runtime: 28 ms, faster than 82.90% of Python3 online submissions for Binary Gap.
#Memory Usage: 14.2 MB, less than 46.52% of Python3 online submissions for Binary Gap.

class Solution:
    def binaryGap(self, n: int) -> int:
        bi = bin(n)[2:]
        max_d = 0
        while bi.count('1') > 1:
            bi = bi[bi.index('1')+1:]
            if bi.index('1') + 1 > max_d:
                max_d = bi.index('1') + 1
        return max_d
