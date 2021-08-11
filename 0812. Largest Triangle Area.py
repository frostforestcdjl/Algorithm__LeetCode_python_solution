#Runtime: 120 ms, faster than 81.69% of Python3 online submissions for Largest Triangle Area.
#Memory Usage: 14.2 MB, less than 84.75% of Python3 online submissions for Largest Triangle Area.

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        tri_list = combinations(points, 3)
        max_area = 0
        for i in tri_list:
            t_area = 0.5*abs((i[1][0]-i[0][0])*(i[2][1]-i[0][1])-(i[2][0]-i[0][0])*(i[1][1]-i[0][1]))
            if t_area > max_area:
                max_area = t_area
        return max_area
