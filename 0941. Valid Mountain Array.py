#Runtime: 180 ms, faster than 99.92% of Python3 online submissions for Valid Mountain Array.
#Memory Usage: 15.6 MB, less than 60.71% of Python3 online submissions for Valid Mountain Array.

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        max_i = arr.index(max(arr))
        if len(arr) < 3 or max_i == 0 or max_i == len(arr)-1:
            return False
        for i in range(max_i, 0, -1):
            if arr[i-1] >= arr[i]:
                return False
        for i in range(max_i, len(arr)-1):
            if arr[i+1] >= arr[i]:
                return False
        return True
