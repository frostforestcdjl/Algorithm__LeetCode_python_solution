#Runtime: 20 ms, faster than 99.61% of Python3 online submissions for Ugly Number.
#Memory Usage: 14.4 MB, less than 10.22% of Python3 online submissions for Ugly Number.

class Solution:
    def isUgly(self, n: int) -> bool:
        if n < 1:
            return False
        while int(n/30) == n/30:
            n = n / 30
        while int(n/15) == n/15:
            n = n / 15
        while int(n/10) == n/10:
            n = n / 10
        while int(n/6) == n/6:
            n = n / 6
        while int(n/5) == n/5:
            n = n / 5
        while int(n/3) == n/3:
            n = n / 3
        while int(n/2) == n/2:
            n = n / 2
        if n == 1:
            return True
        return False
