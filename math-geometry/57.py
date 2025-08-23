# 59. Spiral Matrix II


from enum import Enum
from typing import List
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        '''
        [row][col]
        00 -> 01 -> 02 -/> 03 (bounds)
        down
        12 -> 22 -/> 32 (bounds)
        left
        21 -> 20 -/> 2[-1] (bounds)
        up
        10 -/> 00 (visited)
        right
        11 -/> 12 (visited)

        change direction when move is invalid
        INVALID IF:
        - row >= n || col >= n || row < 0 || col < 0
        - (row, col) in visited set

        END IF:
        - count = n*n (filled all squares)

        DOWN: (-1, 0)
        LEFT: (0, -1)
        UP: (1, 0)
        RIGHT: (0, 1)
        '''
        class dir(Enum):
            DOWN = (1, 0)
            LEFT = (0, -1)
            UP = (-1, 0)
            RIGHT = (0, 1)
        
        def change_dir(curr_dir: dir):
            if curr_dir == dir.RIGHT:
                return dir.DOWN
            elif curr_dir == dir.DOWN:
                return dir.LEFT
            elif curr_dir == dir.LEFT:
                return dir.UP
            else:
                return dir.RIGHT

        def move(curr: tuple, direction: dir):
            dr, dc = direction.value
            row, col = curr[0], curr[1]
            row += dr
            col += dc
            return (row, col)
        
        # track visited cells (row, col)
        visited = set()  
        def is_valid(curr: tuple):
            if curr in visited:
                return False
            if curr[0] < 0 or curr[0] >= n:
                return False
            if curr[1] < 0 or curr[1] >= n:
                return False
            return True
            
        # start rightward
        curr_dir = dir.RIGHT

        res = [[-1] * n for _ in range(n)]

        curr_pos = (0, 0)  # (row, col)
        visited.add((0, 0))
        res[0][0] = 1
        for i in range(n*n):
            new_pos = move(curr_pos, curr_dir)

            if is_valid(new_pos):
                curr_pos = new_pos
                visited.add(curr_pos)
            else:
                new_dir = change_dir(curr_dir)
                new_pos = move(curr_pos, new_dir)
                if is_valid(new_pos):
                    curr_pos = new_pos
                else:
                    continue
                curr_dir = new_dir
                visited.add(curr_pos)
            res[curr_pos[0]][curr_pos[1]] = i+2
        return res