#Runtime: 28 ms, faster than 87.51% of Python3 online submissions for Power of Four.
#Memory Usage: 14.1 MB, less than 87.95% of Python3 online submissions for Power of Four.

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n in [1, 4, 16, 64, 256, 1024, 4096, 16384, 65536, 262144, 1048576, 4194304, 16777216, 67108864, 268435456, 1073741824]:
            return True
        return False
