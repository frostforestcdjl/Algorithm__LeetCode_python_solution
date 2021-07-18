#Runtime: 56 ms, faster than 18.16% of Python3 online submissions for Perfect Number.
#Memory Usage: 14.1 MB, less than 89.43% of Python3 online submissions for Perfect Number.

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 6:
            return False
        left = [1]
        right_new = num
        for i in range(2, int(num**0.5)+1):
            if num%i == 0:
                left.append(i)
                right_new = num//i
            if sum(left) == right_new:
                return True
        return False
