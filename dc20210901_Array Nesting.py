'''
You are given an integer array nums of length n where nums is a permutation of the numbers in the range [0, n - 1].

You should build a set s[k] = {nums[k], nums[nums[k]], nums[nums[nums[k]]], ... } subjected to the following rule:

The first element in s[k] starts with the selection of the element nums[k] of index = k.
The next element in s[k] should be nums[nums[k]], and then nums[nums[nums[k]]], and so on.
We stop adding right before a duplicate element occurs in s[k].
Return the longest length of a set s[k].


Constraints:

1 <= nums.length <= 105
0 <= nums[i] < nums.length
All the values of nums are unique.
'''

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        ind = max_l = temp_count = 0
        cand = [i for i in range(len(nums))]
        while cand:
            if nums[ind] in cand:
                cand.remove(nums[ind])
                temp_count += 1
            else:
                max_l = max(temp_count, max_l)
                temp_count = 0
                ind = cand[0]
            ind = nums[ind]
        return max(temp_count, max_l)
