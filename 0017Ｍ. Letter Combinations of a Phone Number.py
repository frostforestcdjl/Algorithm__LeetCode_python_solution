#Runtime: 28 ms, faster than 85.99% of Python3 online submissions for Letter Combinations of a Phone Number.
#Memory Usage: 14.2 MB, less than 85.28% of Python3 online submissions for Letter Combinations of a Phone Number.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dic = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        letter = []
        if len(digits) == 1:
            for i in dic[digits]:
                letter.append(i)
            return letter

        for i in digits:
            letter.append(dic[i])
            
        return_list = []
        if len(letter) == 2:
            for i in letter[0]:
                for j in letter[1]:
                    return_list.append(i+j)
        
        if len(letter) == 3:
            for i in letter[0]:
                for j in letter[1]:
                    for k in letter[2]:
                        return_list.append(i+j+k)
                    
        if len(letter) == 4:
            for i in letter[0]:
                for j in letter[1]:
                    for k in letter[2]:
                        for l in letter[3]:
                            return_list.append(i+j+k+l)
        return return_list
