#Runtime: 44 ms, faster than 94.82% of Python3 online submissions for Flipping an Image.
#Memory Usage: 14.1 MB, less than 94.62% of Python3 online submissions for Flipping an Image.

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            image[i] = image[i][::-1]
            for j in range(len(image)):
                image[i][j] = 1 - image[i][j]
        return image
