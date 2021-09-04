#Runtime: 28 ms, faster than 87.34% of Python3 online submissions for Valid Boomerang.
#Memory Usage: 14.1 MB, less than 92.86% of Python3 online submissions for Valid Boomerang.

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        return (points[0][0]-points[1][0])*(points[1][1]-points[2][1]) != (points[1][0]-points[2][0])*(points[0][1]-points[1][1])
