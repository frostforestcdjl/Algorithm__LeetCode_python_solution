#Runtime: 84 ms, faster than 99.18% of Python3 online submissions for Group Anagrams.
#Memory Usage: 17.6 MB, less than 63.46% of Python3 online submissions for Group Anagrams.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        for i in strs:
            temp = "".join(sorted(i))
            if temp in dic:
                dic[temp].append(i)
            else:
                dic[temp] = [i]
        return dic.values()
