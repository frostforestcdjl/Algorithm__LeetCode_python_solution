#Runtime: 56 ms, faster than 7.05% of Python3 online submissions for Summary Ranges.
#Memory Usage: 14.3 MB, less than 47.45% of Python3 online submissions for Summary Ranges.

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        pair = []
        result = []
        while len(nums) > 0:
            head = nums[0]
            try:
                while nums[0] + 1 == nums[1]:
                    nums.pop(0)
            except:
                pass
            tail = nums.pop(0)
            pair.append([head, tail])
        for i in range(len(pair)):
            if pair[i][0] == pair[i][1]:
                result.append("%d"%pair[i][0])
            else:
                result.append("%d->%d"%(pair[i][0], pair[i][1]))
        return result
