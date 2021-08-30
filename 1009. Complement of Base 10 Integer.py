#Runtime: 39 ms, faster than 15.31% of Python3 online submissions for Complement of Base 10 Integer.
#Memory Usage: 14.1 MB, less than 67.90% of Python3 online submissions for Complement of Base 10 Integer.

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if not n:
            return 1
        return 2**(int(log(n+0.1)//log(2)) + 1) - n - 1
