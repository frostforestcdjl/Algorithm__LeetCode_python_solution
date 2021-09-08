#Runtime: 28 ms, faster than 79.96% of Python3 online submissions for N-th Tribonacci Number.
#Memory Usage: 14.1 MB, less than 90.06% of Python3 online submissions for N-th Tribonacci Number.

class Solution:
    def tribonacci(self, n: int) -> int:
        t = {0:0, 1:1, 2:1}
        if n < 3:
            return t[n]
        t0, t1, t2 = t[0], t[1], t[2]
        for i in range(n-2):
            t0, t1, t2 = t1, t2, t0 + t1 + t2
        return t2
