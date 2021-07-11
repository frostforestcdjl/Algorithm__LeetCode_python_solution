#Runtime: 28 ms, faster than 76.79% of Python3 online submissions for Nim Game.
#Memory Usage: 13.9 MB, less than 96.73% of Python3 online submissions for Nim Game.

class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4 == 0:
            return False
        return True
