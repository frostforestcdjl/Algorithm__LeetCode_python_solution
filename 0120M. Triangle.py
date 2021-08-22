#Runtime: 52 ms, faster than 94.83% of Python3 online submissions for Triangle.
#Memory Usage: 14.9 MB, less than 87.56% of Python3 online submissions for Triangle.

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(1, len(triangle)):
            triangle[i][0] += triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]
            for j in range(1, len(triangle[i])-1):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])
        return min(triangle[-1])
