class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = 0
        z = []
        try:
            while True:
                x = x*10 + digits.pop(0)
        except:
            y = x + 1
            for i in range(len(str(y))):
                z.append(int(str(y)[i]))
            return z
