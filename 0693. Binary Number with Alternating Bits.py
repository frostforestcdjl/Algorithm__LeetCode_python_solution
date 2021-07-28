#Runtime: 24 ms, faster than 95.08% of Python3 online submissions for Binary Number with Alternating Bits.
#Memory Usage: 14.1 MB, less than 63.19% of Python3 online submissions for Binary Number with Alternating Bits.

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bin_n = bin(n)[2:]
        for i in range(len(bin_n)-1):
            if bin_n[i] == bin_n[i+1]:
                return False
        return True
