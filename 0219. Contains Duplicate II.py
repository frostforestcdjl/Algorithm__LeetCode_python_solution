#Runtime: 572 ms, faster than 41.36% of Python3 online submissions for Contains Duplicate II.
#Memory Usage: 25.9 MB, less than 38.07% of Python3 online submissions for Contains Duplicate II.

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        if len(nums) <= k:
            slice_length = len(nums)
            set_length = len(set(nums))
            if slice_length != set_length:
                return True
            return False
        for i in range(len(nums) - k):
            for_set = nums[i:i+k+1]
            slice_length = len(for_set)
            set_length = len(set(for_set))
            if slice_length != set_length:
                return True  
        return False
