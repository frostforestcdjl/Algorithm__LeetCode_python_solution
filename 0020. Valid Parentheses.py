class Solution:
    def isValid(self, s: str) -> bool:
        x = list(s)
        y = 0
        while (y != len(x)):
            y = len(x)
            for i in range(len(x)-1):
                try:
                    if (x[i] == '(') and (x[i+1] == ')'):
                        x.pop(i)
                        x.pop(i)
                    if (x[i] == '{') and (x[i+1] == '}'):
                        x.pop(i)
                        x.pop(i)
                    if (x[i] == '[') and (x[i+1] == ']'):
                        x.pop(i)
                        x.pop(i)
                except:
                    pass    
        if len(x) != 0:
            return False
        return True
