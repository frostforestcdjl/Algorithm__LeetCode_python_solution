#Runtime: 20 ms, faster than 99.20% of Python3 online submissions for Fibonacci Number.
#Memory Usage: 13.9 MB, less than 97.95% of Python3 online submissions for Fibonacci Number.

class Solution:
    def fib(self, n: int) -> int:
        F = [0, 1]
        if n < 2:
            return F[n]
        for i in range(1, n):
            sumF = F[0] + F[1]
            F[0] = F[1]
            F[1] = sumF
        return sumF
