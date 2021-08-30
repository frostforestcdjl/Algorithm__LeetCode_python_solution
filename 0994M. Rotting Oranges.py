#Runtime: 36 ms, faster than 99.91% of Python3 online submissions for Rotting Oranges.
#Memory Usage: 14.3 MB, less than 38.95% of Python3 online submissions for Rotting Oranges.

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rot = []
        fresh = []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    rot.append([i,j])
                elif grid[i][j] == 1:
                    fresh.append([i,j])
        count = 0
        while rot and fresh:
            new_rot = []
            for cand in rot:
                i, j = cand[0], cand[1]
                if [i-1,j] in fresh:
                    grid[i-1][j] = 2
                    fresh.remove([i-1,j])
                    new_rot.append([i-1,j])
                if [i+1,j] in fresh:
                    grid[i+1][j] = 2
                    fresh.remove([i+1,j])
                    new_rot.append([i+1,j])
                if [i,j-1] in fresh:
                    grid[i][j-1] = 2
                    fresh.remove([i,j-1])
                    new_rot.append([i,j-1])
                if [i,j+1] in fresh:
                    grid[i][j+1] = 2
                    fresh.remove([i,j+1])
                    new_rot.append([i,j+1])
            rot = new_rot
            count += 1
        if fresh:
            return -1
        return count
