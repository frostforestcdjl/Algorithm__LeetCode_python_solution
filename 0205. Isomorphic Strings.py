class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = []
        dic_2 = []
        for i in range(len(s)):
            dic.append([s[i], t[i]])
            dic_2.append([t[i], s[i]])
        dic.sort()
        dic_2.sort()
        print(dic)
        print(dic_2)
        try:
            while True:
                x = dic.count(dic[0])
                if dic[0][0] == dic[x][0]:
                    return False
                else:
                    dic = dic[x:]
        except:
            try:
                while True:
                    x = dic_2.count(dic_2[0])
                    if dic_2[0][0] == dic_2[x][0]:
                        return False
                    else:
                        dic_2 = dic_2[x:]
            except:
                return True
