#Runtime: 24 ms, faster than 95.18% of Python3 online submissions for Hamming Distance.
#Memory Usage: 14.3 MB, less than 43.69% of Python3 online submissions for Hamming Distance.

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x_bin = bin(x)[2:]
        y_bin = bin(y)[2:]
        count = 0
        if len(x_bin) > len(y_bin):
            y_bin = '0'*(len(x_bin) - len(y_bin)) + y_bin
        else:
            x_bin = '0'*(len(y_bin) - len(x_bin)) + x_bin
        for i in range(len(x_bin)):
            if x_bin[i] != y_bin[i]:
                count += 1
        return count
