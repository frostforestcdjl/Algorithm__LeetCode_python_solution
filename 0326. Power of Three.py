#Runtime: 196 ms, faster than 5.33% of Python3 online submissions for Power of Three.
#Memory Usage: 13.9 MB, less than 98.73% of Python3 online submissions for Power of Three.

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        tri = []
        while n >= 3:
            tri.append(n%3)
            n = (n - n%3)/3
        tri.append(n%3)
        
        if tri.count(1) == 1 and tri.count(2) == 0:
            return True
        return False
