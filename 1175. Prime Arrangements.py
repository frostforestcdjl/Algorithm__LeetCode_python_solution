#Runtime: 32 ms, faster than 60.92% of Python3 online submissions for Prime Arrangements.
#Memory Usage: 14.1 MB, less than 84.48% of Python3 online submissions for Prime Arrangements.

class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        prime = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
        c = 0
        for i in range(len(prime)):
            if n < prime[i]:
                break
            else:
                c += 1
        return factorial(n-c)*factorial(c)%(10**9+7)
