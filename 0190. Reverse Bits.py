class Solution:
    def reverseBits(self, n: int) -> int:
        r_s = str(bin(n))[:1:-1]
        r_s = r_s + '0'*(32-len(r_s))
        r = int(r_s, 2)
        return r
