#Runtime: 28 ms, faster than 83.86% of Python3 online submissions for Number Complement.
#Memory Usage: 14 MB, less than 85.83% of Python3 online submissions for Number Complement.

class Solution:
    def findComplement(self, num: int) -> int:
        n = 0
        while 2**n <= num:
            n += 1
        return 2**n - 1 - num
