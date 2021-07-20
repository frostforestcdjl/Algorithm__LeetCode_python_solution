#Runtime: 28 ms, faster than 98.32% of Python3 online submissions for Robot Return to Origin.
#Memory Usage: 14.2 MB, less than 91.75% of Python3 online submissions for Robot Return to Origin.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')
