Runtime: 68 ms, faster than 82.03% of Python3 online submissions for Duplicate Zeros.
Memory Usage: 14.7 MB, less than 85.77% of Python3 online submissions for Duplicate Zeros.

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ind = 0
        while ind < len(arr):
            if arr[ind] == 0:
                arr.insert(ind+1, 0)
                arr.pop()
                ind += 1
            ind += 1
