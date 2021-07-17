Runtime: 60 ms, faster than 97.91% of Python3 online submissions for Relative Ranks.
Memory Usage: 15.1 MB, less than 75.25% of Python3 online submissions for Relative Ranks.

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = []
        rank_dic = {}
        cp_score = [] + score
        cp_score.sort(reverse=True)
        if len(score) == 1:
            return ["Gold Medal"]
        if len(score) == 2:
            if score[0] > score[1]:
                return ["Gold Medal", "Silver Medal"]
            else:
                return ["Silver Medal", "Gold Medal"]
        rank_dic[cp_score[0]] = "Gold Medal"
        rank_dic[cp_score[1]] = "Silver Medal"
        rank_dic[cp_score[2]] = "Bronze Medal"
        for i in range(3, len(cp_score)):
            rank_dic[cp_score[i]] = str(i+1)
        for i in score:
            rank.append(rank_dic[i])
        return rank
