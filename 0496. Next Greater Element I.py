#Runtime: 140 ms, faster than 11.07% of Python3 online submissions for Next Greater Element I.
#Memory Usage: 14.3 MB, less than 90.36% of Python3 online submissions for Next Greater Element I.

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        record = {}
        output = []
        while len(nums2) > 1:
            try:
                record[min(nums2)] = nums2[nums2.index(min(nums2)) + 1]
            except:
                record[min(nums2)] = -1
            nums2.pop(nums2.index(min(nums2)))
        record[min(nums2)] = -1
                              
        for i in nums1:
            output.append(record[i])
        
        return output
