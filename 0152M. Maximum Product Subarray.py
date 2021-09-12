#Runtime: 48 ms, faster than 95.39% of Python3 online submissions for Maximum Product Subarray.
#Memory Usage: 14.4 MB, less than 36.84% of Python3 online submissions for Maximum Product Subarray.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_p = max(nums)
        cand = temp = []
        for i in range(len(nums)):
            if nums[i] != 0:
                temp.append(nums[i])
            elif temp:
                cand.append(temp)
                temp = []
        if temp:
            cand.append(temp)
        for i in cand:
            p = 1
            for j in i:
                p *= j
            if p < 0 and len(i) > 1:
                temp_lv = temp_rv = 1
                for v in i:
                    temp_lv *= v
                    if v < 0:
                        break
                r_i = reversed(i)
                for v in r_i:
                    temp_rv *= v
                    if v < 0:
                        break
                if temp_lv > temp_rv:
                    p = p// temp_lv
                else:
                    p = p// temp_rv
            max_p = max(p, max_p)
        return max_p
