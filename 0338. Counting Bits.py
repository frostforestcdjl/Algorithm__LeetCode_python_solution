#Runtime: 76 ms, faster than 90.94% of Python3 online submissions for Counting Bits.
#Memory Usage: 20.8 MB, less than 90.78% of Python3 online submissions for Counting Bits.

class Solution:
    def countBits(self, n: int) -> List[int]:
        bi_list = []
        for i in range(n + 1):
            bi_list.append(bin(i).count('1'))
        return bi_list
