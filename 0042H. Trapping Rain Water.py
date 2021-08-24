#Runtime: 76 ms, faster than 27.82% of Python3 online submissions for Trapping Rain Water.
#Memory Usage: 15.4 MB, less than 29.47% of Python3 online submissions for Trapping Rain Water.

class Solution:
    def trap(self, height: List[int]) -> int:
        try:
            while height[0] < height[1]:
                height.pop(0)
            while height[-1] < height[-2]:
                height.pop()
        except:
            return 0
        w = 0
        while True:
            max_i = height.index(max(height))
            max_h = height.pop(max_i)
            if not height or max(height) == 0:
                return w
            max2_i = height.index(max(height))
            max2_h = max(height)
            if max2_i >= max_i:
                mi = max_i
            else:
                mi = max2_i + 1
            for i in range(mi, max(max2_i, max_i)):
                w += max2_h - height.pop(mi)
