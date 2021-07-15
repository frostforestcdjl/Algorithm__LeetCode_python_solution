class Solution(object):
    def threeSum(self, A):
        res = []
        A.sort()
        for i in range(len(A) - 2):
            if i > 0 and A[i] == A[i-1]: continue
            l, r = i+1, len(A)-1
            while l < r:
                temp = A[i] + A[l] + A[r]
                if temp > 0: r -= 1
                elif temp < 0: l += 1
                else:
                    res.append((A[i], A[l], A[r]))
                    while l < r and A[l] == A[l+1]: l += 1
                    while l < r and A[r] == A[r-1]: r -= 1
                    l, r = l+1, r-1
        return res
