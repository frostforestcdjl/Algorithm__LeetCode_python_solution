#Runtime: 2692 ms, faster than 5.01% of Python3 online submissions for Longest Harmonious Subsequence.
#Memory Usage: 15.9 MB, less than 78.76% of Python3 online submissions for Longest Harmonious Subsequence.

class Solution:
    def findLHS(self, nums: List[int]) -> int:
        count = []
        sor = sorted(set(nums))
        count.append([sor[0], nums.count(sor[0])])
        
        for i in range(1, len(sor) - 1):
            if sor[i+1] - sor[i] == 1 or sor[i] - sor[i-1] == 1:
                count.append([sor[i], nums.count(sor[i])])
        try:
            if sor[-1] - sor[-2] == 1:
                count.append([sor[-1], nums.count(sor[-1])])
        except:
            pass
        max_set = 0
        for i in range(len(count) - 1):
            if count[i+1][0] -  count[i][0] == 1:
                if count[i][1] + count[i+1][1] > max_set:
                    max_set = count[i][1] + count[i+1][1]
        return max_set
