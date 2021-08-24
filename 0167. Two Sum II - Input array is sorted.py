#Runtime: 60 ms, faster than 83.87% of Python3 online submissions for Two Sum II - Input array is sorted.
#Memory Usage: 14.6 MB, less than 86.78% of Python3 online submissions for Two Sum II - Input array is sorted.
    
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in set(numbers):
            ind = numbers.index(i)
            test_l = numbers[:ind] + numbers[ind+1:]
            if target - i in test_l:
                r2 = numbers.index(target - i)
                if numbers.index(target - i) == ind:
                    return ind + 1, ind + 2
                return min(ind, r2) + 1, max(ind, r2) + 1
            

class Solution2:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            if numbers.count(numbers[i]) > 2:
                pass
            else:
                for j in range(i+1, len(numbers)):
                    if numbers[i] + numbers[j] == target:
                        return [i+1, j+1]
