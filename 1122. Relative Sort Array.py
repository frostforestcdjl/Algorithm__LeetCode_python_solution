#Runtime: 32 ms, faster than 90.72% of Python3 online submissions for Relative Sort Array.
#Memory Usage: 14.3 MB, less than 67.25% of Python3 online submissions for Relative Sort Array.

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        cand = []
        for i in arr2:
            while i in arr1:
                cand.append(arr1.pop(arr1.index(i)))
        if arr1:
            cand += sorted(arr1)
        return cand
