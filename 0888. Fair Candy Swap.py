#Runtime: 336 ms, faster than 99.20% of Python3 online submissions for Fair Candy Swap.
#Memory Usage: 16.7 MB, less than 63.96% of Python3 online submissions for Fair Candy Swap.

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes))//2
        sb = set(bobSizes)
        for i in aliceSizes:
            if i - diff in sb:
                return i, i - diff
