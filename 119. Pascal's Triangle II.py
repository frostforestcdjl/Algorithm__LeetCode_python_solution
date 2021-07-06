class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def comb(n, k):
            c = 1
            for i in range(n-k):
                c = c * (i + k + 1) / (i + 1)
            return int(c)
        temp = []
        for j in range(rowIndex+1):
            temp.append(comb(rowIndex, j))
        return temp
