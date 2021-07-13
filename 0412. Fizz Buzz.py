#Runtime: 32 ms, faster than 99.11% of Python3 online submissions for Fizz Buzz.
#Memory Usage: 15.1 MB, less than 64.81% of Python3 online submissions for Fizz Buzz.

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        out_list = []
        for i in range(1, n+1):
            temp = ""
            if i%3 == 0:
                temp += "Fizz"
            if i%5 == 0:
                temp += "Buzz"
            if i%3*i%5 != 0:
                temp += str(i)
            out_list.append(temp)
        return out_list
