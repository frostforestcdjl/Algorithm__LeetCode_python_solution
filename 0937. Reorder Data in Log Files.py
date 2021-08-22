#Runtime: 36 ms, faster than 70.72% of Python3 online submissions for Reorder Data in Log Files.
#Memory Usage: 14.4 MB, less than 65.66% of Python3 online submissions for Reorder Data in Log Files.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        let = []
        dig = []
        for i in logs:
            i_list = i.split(' ')
            if i_list[1].isalpha():
                let.append(i_list)
            else:
                dig.append(i)
        let = sorted(let, key=lambda x:x[1:])
        i = 0
        while i < len(let)-1:
            if let[i][1:] == let[i+1][1:]:
                k = 0
                while let[i+k][1:] == let[i+k+1][1:]:
                    k += 1
                let[i:i+k+1] = sorted(let[i:i+k+1])
                i += k
            i += 1
        for i in range(len(let)):
            let[i] = ' '.join(let[i])
        return let + dig
