#Runtime: 60 ms, faster than 27.07% of Python3 online submissions for Intersection of Two Arrays.
#Memory Usage: 14.1 MB, less than 97.66% of Python3 online submissions for Intersection of Two Arrays.

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1).intersection(set(nums2))
