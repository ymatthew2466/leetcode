# 994. Rotting Oranges


from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        iterate over rows:
            iterate over cols:
                if (row, col) not in visited and grid[row][col] == 2:
                    # rotten
                    bfs(row, col)

        '''
        visited = set()

        def get_neighbors(r, c):
            indices = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            res = []
            for row, col in indices:
                if (row, col) not in visited: # unique
                    if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]): # bounds
                        if grid[row][col] == 1: # fresh orange
                            res.append((row, col))
            return res


        q = deque()
        fresh = 0
        mins = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    # multi-source bfs, add all sources to queue
                    q.append((row, col))
                
                if grid[row][col] == 1:
                # count num of fresh as end condition
                    fresh += 1
        
        # BFS:
        while len(q) > 0 and fresh > 0:
            # process all oranges of current time step
            for _ in range(len(q)):  # get everything from current level
                r, c = q.popleft()
                for r1, c1 in get_neighbors(r, c):
                    if (r1, c1) not in visited and grid[r1][c1] == 1:
                        visited.add((r1, c1))  # set visited
                        q.append((r1, c1))  # add neighbor to queue
                        grid[r1][c1] = 2  # rot orange
                        fresh -= 1  # decrement fresh count
            # ensure this is PER LEVEL (minute)
            mins += 1
        
        # check if any remaining fresh oranges (fail)
        fresh = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    fresh = True
        if fresh:
            return -1
        else:
            return mins