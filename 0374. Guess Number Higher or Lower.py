#Runtime: 40 ms, faster than 12.65% of Python3 online submissions for Guess Number Higher or Lower.
#Memory Usage: 14.1 MB, less than 90.03% of Python3 online submissions for Guess Number Higher or Lower.

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return 1
        i = 2
        guess_n = round(n/i + 0.1)
        while guess(guess_n) != 0:
            direction = guess(guess_n)
            i *= 2
            guess_n += round(n/i + 0.1) * direction
        return guess_n
