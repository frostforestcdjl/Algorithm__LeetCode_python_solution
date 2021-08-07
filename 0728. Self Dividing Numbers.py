#Runtime: 40 ms, faster than 92.72% of Python3 online submissions for Self Dividing Numbers.
#Memory Usage: 14.4 MB, less than 30.16% of Python3 online submissions for Self Dividing Numbers.

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        if right < 10:
            return [i for i in range(left, right + 1)]
        cand = []
        for i in range(left, right + 1):
            divisor = set(str(i))
            if '0' not in divisor:
                divisible = True
                for j in divisor:
                    if i%int(j) != 0:
                        divisible = False
                        break
                if divisible == True:
                    cand.append(i)
        return cand
                
