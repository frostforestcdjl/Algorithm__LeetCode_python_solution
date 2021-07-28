#Runtime: 164 ms, faster than 36.89% of Python3 online submissions for Employee Importance.
#Memory Usage: 15.1 MB, less than 99.97% of Python3 online submissions for Employee Importance.

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        sum_imp = 0
        id_list = [id]      
        while len(id_list) > 0: 
            for i in range(len(employees)):
                if employees[i].id in id_list:
                    sum_imp += employees[i].importance
                    id_list += employees[i].subordinates
                    id_list.remove(employees[i].id)
        return sum_imp
