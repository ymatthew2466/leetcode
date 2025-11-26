# 1267. Count Servers that Communicate


from typing import List
class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        '''
        bfs
        iterate thru grid
            if not visited and server:
                bfs 
        bfs:
            visit neighbors and mark all as visited and increment count
        '''
        visited = set()
        count = 0

        def get_neighbors(row, col):
            res = []
            # explore entire row
            for c1 in range(len(grid[0])):
                cell = grid[row][c1]
                if (row, c1) not in visited:
                    if cell == 1:
                        res.append((row,c1))
            # explore entire col
            for r1 in range(len(grid)):
                cell = grid[r1][col]
                if (r1, col) not in visited:
                    if cell == 1:
                        res.append((r1, col))
            return res

        def bfs(row, col):
            nonlocal count
            q = deque()
            q.append((row, col))
            first = True
            while len(q)>0:
                curr = q.popleft()
                r0, c0 = curr
                visited.add(curr)
                neighbors = get_neighbors(r0,c0)
                if first and len(neighbors)>0:
                    count += 1
                first = False
                for neighbor in neighbors:
                    count += 1
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
                

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if (row, col) not in visited and grid[row][col] == 1:
                    bfs(row, col)
        return(count)