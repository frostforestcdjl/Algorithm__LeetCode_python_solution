#Runtime: 44 ms, faster than 94.77% of Python3 online submissions for 1-bit and 2-bit Characters.
#Memory Usage: 14.1 MB, less than 90.57% of Python3 online submissions for 1-bit and 2-bit Characters.

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        count_0 = 0
        if bits.count(0) > 1:
            for i in range(len(bits)):
                if bits[~i] == 0:
                    count_0 += 1
                if count_0 == 2:
                    if i % 2 == 1:
                        return True
                    else:
                        return False
        if len(bits) % 2 == 1:
            return True
        return False
