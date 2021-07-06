class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, maxArea = 0, len(height)-1, 0
        hmax = max(height)
        while (l<r and (r-l)*hmax > maxArea):
            maxArea = max(maxArea, min(height[l], height[r])*(r-l))
            if (height[l] < height[r]):
                l+=1
            elif (height[l] > height[r]):
                r-=1
            else:
                l+=1
                r-=1
        return maxArea
