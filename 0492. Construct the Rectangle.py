#Runtime: 24 ms, faster than 98.36% of Python3 online submissions for Construct the Rectangle.
#Memory Usage: 14.2 MB, less than 69.10% of Python3 online submissions for Construct the Rectangle.

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        a = int(area**0.5)
        while a > 0:
            if area/a == area//a:
                return [area//a, a]
            a -= 1
