#Runtime: 756 ms, faster than 98.28% of Python3 online submissions for Distribute Candies.
#Memory Usage: 16.3 MB, less than 58.92% of Python3 online submissions for Distribute Candies.

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType)//2, len(set(candyType)))
