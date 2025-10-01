# 2658. Maximum Number of Fish in a Grid


from collections import deque
from typing import List
class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        '''
        iterate over grid:
            at each water cell (not visited): 
                bfs (returns count)
        
        def bfs(row, col):
            ...
        '''

        visited = set()
        mx = float("-inf")

        def get_neighbors(r, c):
            indices = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            res = []
            for r1, c1 in indices:
                if r1 >= 0 and r1 < len(grid) and c1 >= 0 and c1 < len(grid[0]):
                    if (r1, c1) not in visited and grid[r1][c1] > 0:
                        res.append((r1, c1))
            return res

        def bfs(r, c):  # output num fish (int)
            count = 0
            q = deque()
            q.append((r,c))
            visited.add((r,c))

            while len(q)>0:
                r1, c1 = q.popleft()
                count += grid[r1][c1]
                # look at neighbors
                for r2, c2 in get_neighbors(r1, c1):
                    q.append((r2, c2))
                    visited.add((r2, c2))
            return count

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] > 0:
                    count = bfs(row, col)
                    mx = max(count, mx)
        return max(mx, 0)
        