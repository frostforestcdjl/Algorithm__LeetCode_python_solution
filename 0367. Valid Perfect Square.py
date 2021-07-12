#Runtime: 24 ms, faster than 95.28% of Python3 online submissions for Valid Perfect Square.
#Memory Usage: 14.1 MB, less than 67.08% of Python3 online submissions for Valid Perfect Square.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num**0.5)%1 == 0:
            return True
        return False
