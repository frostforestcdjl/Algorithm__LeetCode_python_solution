#Runtime: 556 ms, faster than 90.31% of Python3 online submissions for Image Smoother.
#Memory Usage: 14.8 MB, less than 78.06% of Python3 online submissions for Image Smoother.

class Solution:
    def imageSmoother(self, img):
        smoother = [[] for i in range(len(img))]
        for i in range(len(img)):
            for j in range(len(img[0])):
                count = 0
                if i == 0 or j == 0:
                    TL = 0
                else:
                    TL = img[i-1][j-1]
                    count += 1
                if i == 0:
                    TM = 0
                else:
                    TM = img[i-1][j]
                    count += 1
                if i == 0 or j == len(img[0])-1:
                    TR = 0
                else:
                    TR = img[i-1][j+1]
                    count += 1
                if j == 0:
                    ML = 0
                else:
                    ML = img[i][j-1]
                    count += 1
                MM = img[i][j]
                count += 1
                if j == len(img[0]) - 1:
                    MR = 0
                else:
                    MR = img[i][j+1]
                    count += 1
                if i == len(img) - 1 or j == 0:
                    BL = 0
                else:
                    BL = img[i+1][j-1]
                    count += 1
                if i == len(img) - 1:
                    BM = 0
                else:
                    BM = img[i+1][j]
                    count += 1
                if i == len(img) - 1 or j == len(img[0]) - 1:
                    BR = 0
                else:
                    BR = img[i+1][j+1]
                    count += 1
                    
                smoother[i].append((TL + TM + TR + ML + MM + MR + BL + BM + BR)//count)
        return smoother
