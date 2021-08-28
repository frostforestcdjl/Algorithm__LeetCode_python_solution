#Runtime: 120 ms, faster than 96.98% of Python3 online submissions for Max Area of Island.
#Memory Usage: 14.5 MB, less than 87.06% of Python3 online submissions for Max Area of Island.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_i = 0
        for i in range(len(grid)):
            while 1 in grid[i]:
                temp = 1
                start = grid[i].index(1)
                grid[i][start] = 2
                stack = [[i, start]]
                while start+1 < len(grid[0]) and grid[i][start+1] == 1:
                    temp += 1
                    start += 1
                    grid[i][start] = 2
                    stack.append([i, start])
                while stack:
                    if stack[0][0]-1 >= 0 and grid[stack[0][0]-1][stack[0][1]] == 1:
                        temp += 1
                        grid[stack[0][0]-1][stack[0][1]] = 2
                        stack.append([stack[0][0]-1, stack[0][1]])
                    if stack[0][1]-1 >= 0 and grid[stack[0][0]][stack[0][1]-1] == 1:
                        temp += 1
                        grid[stack[0][0]][stack[0][1]-1] = 2
                        stack.append([stack[0][0], stack[0][1]-1])
                    if stack[0][0]+1 < len(grid) and grid[stack[0][0]+1][stack[0][1]] == 1:
                        temp += 1
                        grid[stack[0][0]+1][stack[0][1]] = 2
                        stack.append([stack[0][0]+1, stack[0][1]])
                    if stack[0][1]+1 < len(grid[0]) and grid[stack[0][0]][stack[0][1]+1] == 1:
                        temp += 1
                        grid[stack[0][0]][stack[0][1]+1] = 2
                        stack.append([stack[0][0], stack[0][1]+1])
                    stack.pop(0)
                max_i = max(max_i, temp)
        return max_i
