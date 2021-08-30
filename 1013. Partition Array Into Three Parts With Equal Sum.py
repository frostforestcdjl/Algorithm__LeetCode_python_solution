#Runtime: 320 ms, faster than 42.64% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.
#Memory Usage: 20.9 MB, less than 94.75% of Python3 online submissions for Partition Array Into Three Parts With Equal Sum.

class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        if sum(arr)//3 != sum(arr)/3:
            return False
        part = sum(arr)//3
        s = count = 0
        for i in arr:
            s += i
            if s == part:
                count += 1
                s = 0
        return count >= 3
