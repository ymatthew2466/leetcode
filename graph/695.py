# 695. Max Area of Island

from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        iterate thru rows
            iterate thru cols
                cell = grid[row][col]
                if (row,col) not visited and cell == 1:
                    area = bfs(row, col)  # bfs returns area of THIS island
                    max_area = max(max_area, area)
        
        '''
        visited = set()

        def get_neighbors(tup):
            r, c = tup
            indices = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            res = []
            for index in indices:
                r1, c1 = index
                if r1 >= 0 and r1 < len(grid) and c1>=0 and c1<len(grid[0]):  # bounds
                    if grid[r1][c1] == 1:  # part of island
                        res.append((r1, c1))
            return res

        def bfs(row, col):
            # q = deque()
            q = []
            q.append((row, col))
            area = 0

            while len(q) > 0:
                # curr = q.popleft()
                curr = q.pop()
                visited.add(curr)
                # do some operation here
                area += 1

                for neighbor in get_neighbors(curr):
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
            return area
        
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row,col) not in visited and grid[row][col] == 1:
                    area = bfs(row, col)  # bfs returns area of THIS island
                    max_area = max(area, max_area)
        return max_area
