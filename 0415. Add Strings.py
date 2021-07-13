#Runtime: 40 ms, faster than 72.94% of Python3 online submissions for Add Strings.
#Memory Usage: 14.4 MB, less than 63.60% of Python3 online submissions for Add Strings.

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = []
        l2 = []
        for i in num1:
            l1.append(ord(i)-48)
        for i in num2:
            l2.append(ord(i)-48)
        over = 0
        s = ''
        l1.reverse()
        l2.reverse()
        for i in range(min(len(l1), len(l2))):
            s = str(int((l1[i] + l2[i] + over)%10)) + s
            over = ((l1[i] + l2[i] + over) - (l1[i] + l2[i] + over)%10)//10
        for i in range(min(len(l1), len(l2)), min(len(l1), len(l2)) + abs(len(l1)-len(l2))):
            if len(l1) > len(l2):
                s = str(int((l1[i] + over)%10)) + s
                over = (l1[i] + over - (l1[i] + over)%10)//10
            else:
                s = str(int((l2[i] + over)%10)) + s
                over = (l2[i] + over - (l2[i] + over)%10)//10
        if over != 0:
            s = str(over) + s
        return s
