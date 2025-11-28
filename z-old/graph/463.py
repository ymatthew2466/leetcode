# 463. Island Perimeter

from collections import deque
from typing import List
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        '''
        bfs

        find the first i,j where grid[i][j] == 1 (starting vertex)
        maintain set of visited ((i, j))
        maintain deque to store next vertices to visit: q = deque()

        find neighbors of each vertex, and calculate its perimeter (if applicable)
        '''
        # get neighbors of a cell
        def neighbors(row, col):
            indices = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            out = []
            for row, col in indices:
                if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                    if (grid[row][col] == 1):  # must be land
                        out.append((row, col))
            return out
        
        def find_perimeter(row, col):
            '''
            perimeter is just how much water or edge is exposed to each block
            '''
            indices = [(row+1, col), (row-1, col), (row, col+1), (row, col-1)]
            count = 0
            for row, col in indices:
                # if out of bounds
                if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                    count += 1
                elif grid[row][col] == 0:
                    count += 1
            return count

        # find first land
        start = None
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    start = (row, col)
                    break
        
        visited = set()
        q = deque()
        q.append(start)
        perimeter = 0
        while len(q) > 0:
            curr = q.popleft()
            visited.add(curr)
            # add perimeter of curr
            perimeter += find_perimeter(curr[0], curr[1])
            for r, c in neighbors(curr[0], curr[1]):
                if (r, c) not in visited:
                    # add to queue
                    q.append((r, c))
                    visited.add((r,c))
        return(perimeter)