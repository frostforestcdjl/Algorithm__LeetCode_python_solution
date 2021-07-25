#Runtime: 5244 ms, faster than 5.06% of Python3 online submissions for Combination Sum.
#Memory Usage: 148.9 MB, less than 6.31% of Python3 online submissions for Combination Sum.

class Solution:
    def combinationSum(self, candidates, target: int):
        while min(candidates) > target:
            return []
        candidates.sort(reverse = True)
        while candidates[0] > target:
            candidates.pop(0)
        comb = [[0] for i in range(len(candidates))]
        for i in range(len(candidates)):
            cut = 0 + len(comb)
            for k in range(cut):
                temp_target = target - comb[k][0]
                for j in range(temp_target//candidates[i] + 1):
                    comb.append(comb[k] + [[j, candidates[i]]])
                    comb[-1][0] += j*candidates[i]
            comb = comb[cut:]
        i = 0
        while i < len(comb):
            try:
                while comb[i][0] != target:
                    comb.pop(i)
            except:
                pass
            i += 1
        comb_temp = []
        for i in comb:
            temp = []
            for j in range(1, len(i)):
                temp += i[j][0]*[i[j][1]]
            if temp not in comb_temp:
                comb_temp.append(temp)
        return comb_temp
