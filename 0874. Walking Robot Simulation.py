#Runtime: 6960 ms, faster than 5.10% of Python3 online submissions for Walking Robot Simulation.
#Memory Usage: 19.6 MB, less than 97.17% of Python3 online submissions for Walking Robot Simulation.

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        ob_x = [obstacles[i][0] for i in range(len(obstacles))]
        ob_y = [obstacles[i][1] for i in range(len(obstacles))]
        x = y = vx = 0
        vy = 1
        max_d = 0
        for i in commands:
            if i == -2:
                vx, vy = -vy, vx
            if i == -1:
                vx, vy = vy, -vx
            if i > 0:
                if vx == 0:
                    if x in ob_x:
                        temp_ob = []
                        for j in obstacles:
                            if j[0] == x:
                                temp_ob.append(j[1])
                        for j in range(1, i+1):
                            if y + vy in temp_ob:
                                break
                            else:
                                y += vy
                    else:
                        y += vy*i
                else:
                    if y in ob_y:
                        temp_ob = []
                        for j in obstacles:
                            if j[1] == y:
                                temp_ob.append(j[0])
                        for j in range(1, i+1):
                            if x + vx in temp_ob:
                                break
                            else:
                                x += vx
                    else:
                        x += vx*i
                if x**2 + y**2 > max_d:
                    max_d = x**2 + y**2
        return max_d
