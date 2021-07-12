#Runtime: 60 ms, faster than 31.18% of Python3 online submissions for Intersection of Two Arrays II.
#Memory Usage: 14.4 MB, less than 70.10% of Python3 online submissions for Intersection of Two Arrays II.

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list_inter = []
        inter = set(nums1).intersection(set(nums2))
        for i in inter:
            list_inter += min(nums1.count(i), nums2.count(i)) * [i]
        return list_inter
