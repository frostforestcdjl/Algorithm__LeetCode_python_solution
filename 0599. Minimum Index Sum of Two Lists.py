#Runtime: 232 ms, faster than 34.07% of Python3 online submissions for Minimum Index Sum of Two Lists.
#Memory Usage: 14.7 MB, less than 87.93% of Python3 online submissions for Minimum Index Sum of Two Lists.

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_index = len(list1) + len(list2)
        res_list = []
        for i in set(list1).intersection(set(list2)):
            if list1.index(i) + list2.index(i) < min_index:
                min_index = list1.index(i) + list2.index(i)
                res_list = [i]
            elif list1.index(i) + list2.index(i) == min_index:
                res_list.append(i)
        return res_list
