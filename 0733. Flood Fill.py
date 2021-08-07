#Runtime: 72 ms, faster than 83.20% of Python3 online submissions for Flood Fill.
#Memory Usage: 14.3 MB, less than 76.39% of Python3 online submissions for Flood Fill.

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        old_c = image[sr][sc]
        image[sr][sc] = newColor
        front = [[sr, sc]]
        
        while len(front) > 0:
            temp_front = []
            for i in front:
                if i[0]-1 >= 0 and image[i[0]-1][i[1]] == old_c:
                    image[i[0]-1][i[1]] = newColor
                    temp_front.append([i[0]-1, i[1]])
                if i[0]+1 < len(image) and image[i[0]+1][i[1]] == old_c:
                    image[i[0]+1][i[1]] = newColor
                    temp_front.append([i[0]+1, i[1]])
                if i[1]-1 >= 0 and image[i[0]][i[1]-1] == old_c:
                    image[i[0]][i[1]-1] = newColor
                    temp_front.append([i[0], i[1]-1])
                if i[1]+1 < len(image[0]) and image[i[0]][i[1]+1] == old_c:
                    image[i[0]][i[1]+1] = newColor
                    temp_front.append([i[0], i[1]+1])
            front = temp_front
        return image
