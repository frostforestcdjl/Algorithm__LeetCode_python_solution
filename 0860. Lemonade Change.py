#Runtime: 796 ms, faster than 37.79% of Python3 online submissions for Lemonade Change.
#Memory Usage: 18.7 MB, less than 18.16% of Python3 online submissions for Lemonade Change.

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        c5 = c10 = 0
        for i in bills:
            if i == 5:
                c5 += 1
            elif i == 10:
                c5 -= 1
                c10 += 1
            elif c10 > 0:
                c10 -= 1
                c5 -= 1
            else:
                c5 -= 3
            if c5 < 0 or c10 < 0:
                return False
        return True
