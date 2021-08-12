#Runtime: 28 ms, faster than 82.44% of Python3 online submissions for Rectangle Overlap.
#Memory Usage: 14 MB, less than 98.56% of Python3 online submissions for Rectangle Overlap.

class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        if rec2[0] >= rec1[2] or rec1[0] >= rec2[2] or rec2[1] >= rec1[3] or rec1[1] >= rec2[3]:
                return False
        return True
