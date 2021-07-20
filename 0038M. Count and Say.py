#Runtime: 40 ms, faster than 89.48% of Python3 online submissions for Count and Say.
#Memory Usage: 14.2 MB, less than 75.07% of Python3 online submissions for Count and Say.

class Solution:
    def countAndSay(self, n: int) -> str:
        say = '1'
        for i in range(n-1):
            temp = []
            while len(say) > 0:
                count_temp = 1
                try:
                    while say[0] == say[count_temp]:
                        count_temp += 1
                except:
                    pass
                temp.append(str(count_temp))
                temp.append(say[0])
                say = say[count_temp:]
            say = ''.join(temp)
        return say
