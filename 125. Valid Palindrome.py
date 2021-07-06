class Solution:
    def isPalindrome(self, s: str) -> bool:
        list_s = list(s.lower())
        ab = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        clean_list = []
        
        for i in range(len(list_s)):
            temp_ab = []
            try:
                temp_ab = temp_ab + ab
                temp_ab.remove(list_s[i])
                clean_list.append(list_s[i])
            except:
                pass

        for i in range(int((len(clean_list)%2 + len(clean_list))/2)):
            if clean_list[i] != clean_list[-(i+1)]:
                return False
        return True
