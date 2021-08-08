#Runtime: 208 ms, faster than 78.14% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.
#Memory Usage: 13.9 MB, less than 99.19% of Python3 online submissions for Prime Number of Set Bits in Binary Representation.

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        count = 0
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        for i in range(left, right+1):
            if bin(i)[2:].count('1') in prime:
                count += 1
        return count
