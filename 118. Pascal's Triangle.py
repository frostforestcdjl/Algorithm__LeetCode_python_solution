class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def comb(n, k):
            c = 1
            for i in range(n-k):
                c = c * (i + k + 1) / (i + 1)
            return int(c)
        pas = []
        for i in range(numRows):
            temp = []
            for j in range(i+1):
                temp.append(comb(i, j))
            pas.append(temp)
        return pas
