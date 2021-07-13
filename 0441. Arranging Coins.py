#Runtime: 24 ms, faster than 99.16% of Python3 online submissions for Arranging Coins.
#Memory Usage: 14.2 MB, less than 65.58% of Python3 online submissions for Arranging Coins.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((sqrt(1+8*n) - 1)/2)
