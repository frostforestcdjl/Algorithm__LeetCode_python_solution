class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        
        mid = int((len(nums)-1)/2)
        try:
            while (nums[mid] == nums[mid + 1]) or (nums[mid] == nums[mid - 1]):
                if (nums[0] != nums[1]):
                    return nums[0]
                elif (nums[-1] != nums[-2]):
                    return nums[-1]
                if nums[mid - mid%2] == nums[mid - mid%2 + 1]:
                    nums = nums[mid - mid%2:]
                    mid = int((len(nums)-1)/2)
                else:
                    nums = nums[:mid + mid%2 + 1]
                    mid = int((len(nums)-1)/2)
        except:
            return nums[mid]
        return nums[mid]
