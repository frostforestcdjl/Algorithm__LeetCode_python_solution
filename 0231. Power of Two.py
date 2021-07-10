#Runtime: 32 ms, faster than 68.91% of Python3 online submissions for Power of Two.
#Memory Usage: 14 MB, less than 88.49% of Python3 online submissions for Power of Two.

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        if bin(n).count('1') == 1:
            return True
        return False
