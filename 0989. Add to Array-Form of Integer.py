#Runtime: 248 ms, faster than 99.52% of Python3 online submissions for Add to Array-Form of Integer.
#Memory Usage: 15.1 MB, less than 74.89% of Python3 online submissions for Add to Array-Form of Integer.

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        r = k%10
        q = (k-r)//10
        for i in range(len(num)):
            if num[~i] + r >= 10:
                q += 1
                r -= 10
            num[~i] += r
            r = q%10
            q = (q-r)//10
            if q == 0 and r == 0:
                break
        if r != 0 or q != 0:
            num = [int(i) for i in str(q)] + [r] + num
            if num[0] == 0:
                num.pop(0)
        return num
