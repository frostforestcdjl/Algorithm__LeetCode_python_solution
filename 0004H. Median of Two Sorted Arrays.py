class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        x = nums1 + nums2
        if len(nums1) + len(nums2) == 1:
            return x[0]
        x.sort()
        return (x[int((len(x) + len(x)%2)/2 - 1)] + x[int(-((len(x) + len(x)%2)/2))]) / 2
