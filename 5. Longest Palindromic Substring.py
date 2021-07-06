class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ''
        if len(s) <= 1:
            return s

        temp_max = []
        s_list = list(s)
        for i in range(len(s_list)):
            if i >= len(s_list):
                break
            same_letter = 0
            try:
                while s_list[i] == s_list[i + 1]:             
                    s_list.pop(i)
                    same_letter += 1
            except:
                pass
            same_letter += 1
            s_list.insert(i+1, [str(same_letter), s_list[i]])
            s_list.pop(i)
            temp_max.append(same_letter)
                    
        length = max(temp_max)
        i_j_v_d_record = []
        replace = False
        ult_break = False
       
        for i in range(len(s_list)):  
            if ult_break == False:
                for j in range(1, len(s_list) - i + 1):
                    if ult_break == False:
                        k = 0
                        try:
                            while (s_list[i+k][0] == s_list[-(j+k)][0]) and (s_list[i+k][1] == s_list[-(j+k)][1]) and (2*k <= (len(s_list) - i - j)):
                                k += 1
                            if len(s_list) - i - j < 2*k:
                                temp_lengh = 0
                                for w in range(i, len(s_list) - j + 1):
                                    temp_lengh += int(s_list[w][0])

                                keep_checking = True
                                v = 0
                                d = 0
                                while ((-j+1+v) < 0) and ((i-1-v) >= 0) and (s_list[i-1-v][1] == s_list[-j+1+v][1]) and keep_checking == True:
                                    if s_list[i-1-v][0] == s_list[-j+1+v][0]:
                                        d += int(s_list[i-1-v][0])
                                        temp_lengh += int(s_list[i-1-v][0])*2
                                        keep_checking = True
                                    else:
                                        d += min(int(s_list[i-1-v][0]), int(s_list[-j+1+v][0]))
                                        temp_lengh += min(int(s_list[i-1-v][0]), int(s_list[-j+1+v][0]))*2
                                        keep_checking = False
                                    v += 1

                                if temp_lengh > length:
                                    length = temp_lengh
                                    i_j_v_d_record = [i, j, v, d]
                                    replace = True
                                    if length > len(s)/2:
                                        ult_break = True
                        except:
                            pass
                    else:
                        break
            else:
                break
        if replace == False:
            i_j_v_d_record = [s_list.index(max(s_list)), s_list.index(max(s_list)) + 1, 0, 0]
        front_n = 0
        for i in range(i_j_v_d_record[0]):
            front_n += int(s_list[i][0])
        front_n -= i_j_v_d_record[3]

        return s[front_n:front_n+length]
