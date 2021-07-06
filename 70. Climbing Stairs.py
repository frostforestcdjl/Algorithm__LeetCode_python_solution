class Solution:
    def climbStairs(self, n: int) -> int:
        def factor(x):
            j = 1
            for i in range(x):
                j = j * (i + 1)
            return j
        
        def comb(n, k):
            return int(factor(n)/(factor(k)*factor(n-k)))
        
        ways = 0      
        for i in range(int((n - (n%2))/2) + 1):
            ways = ways + comb(int(n) - i, i)
        return ways
            
