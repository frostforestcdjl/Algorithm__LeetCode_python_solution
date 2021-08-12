#Runtime: 72 ms, faster than 80.91% of Python3 online submissions for Peak Index in a Mountain Array.
#Memory Usage: 15.1 MB, less than 96.79% of Python3 online submissions for Peak Index in a Mountain Array.

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return arr.index(max(arr))

      
#Runtime: 60 ms, faster than 99.68% of Python3 online submissions for Peak Index in a Mountain Array.
#Memory Usage: 15.4 MB, less than 19.70% of Python3 online submissions for Peak Index in a Mountain Array.

class Solution2:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = 0
        r = len(arr)
        index = len(arr)//2
        while arr[index-1] > arr[index] or arr[index+1] > arr[index]:
            if arr[index-1] > arr[index]:
                r = index
            else:
                l = index
            index = (l + r)//2
        return index

      
#Runtime: 60 ms, faster than 99.68% of Python3 online submissions for Peak Index in a Mountain Array.
#Memory Usage: 15.6 MB, less than 9.20% of Python3 online submissions for Peak Index in a Mountain Array.

class Solution3:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l = index = len(arr)//2
        while arr[index-1] > arr[index] or arr[index+1] > arr[index]:
            l = l//2
            if l < 1:
                l = 1
            if arr[index-1] > arr[index]:
                index -= l
            else:
                index += l
        return index
