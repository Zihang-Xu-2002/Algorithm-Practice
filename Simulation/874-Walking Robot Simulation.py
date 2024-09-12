from typing import List

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # 定义四个方向：北、东、南、西
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # 北, 东, 南, 西
        direction = 0  # 初始方向为北
        place = [0, 0]  # 初始位置
        obstacle_set = set(map(tuple, obstacles))  # 将障碍物转换为集合
        
        max_distance = 0  # 用于记录最大的欧几里得距离的平方

        for command in commands:
            if command == -2:  # 左转90度
                direction = (direction - 1) % 4
            elif command == -1:  # 右转90度
                direction = (direction + 1) % 4
            else:  # 前进
                for step in range(command):
                    next_x = place[0] + directions[direction][0]
                    next_y = place[1] + directions[direction][1]
                    
                    if (next_x, next_y) not in obstacle_set:
                        place[0], place[1] = next_x, next_y
                        max_distance = max(max_distance, place[0]**2 + place[1]**2)
                    else:
                        break
        
        return max_distance