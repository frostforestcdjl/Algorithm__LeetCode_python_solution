#Runtime: 2176 ms, faster than 5.22% of Python3 online submissions for Can Place Flowers.
#Memory Usage: 14.3 MB, less than 99.22% of Python3 online submissions for Can Place Flowers.

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        avalible = 0
        while flowerbed.count(0) > 0:
            if flowerbed[0] == 1:
                flowerbed = flowerbed[flowerbed.index(0)+1:]
            else:
                try:
                    avalible += ((flowerbed.index(1) - 1) + (flowerbed.index(1) - 1)%2)//2
                    flowerbed = flowerbed[flowerbed.index(1):]
                except:
                    avalible += (len(flowerbed) + len(flowerbed)%2)//2
                    break
        return avalible >= n
