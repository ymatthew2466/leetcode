# 200. Number of Islands


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        bfs

        iterate across rows:
            iterate across cols:
                if cell == 1 AND cell not visited:
                    count += 1
                    BFS (marks every connected 1 as visited)


        def BFS(starter cell):
            queue = deque()
            queue.append(cell)
            visited.add(cell)

            while queue:
                curr = queue.popleft()
                visited.add(curr)  # this is wrong
                r, c = curr
                for neighbor of cell:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        ''' 
        visited = set()
        count = 0

        def get_neighbors(r, c):
            indicies = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            res = []
            for row, col in indicies:
                if row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]):
                    if (row, col) not in visited and grid[row][col] == "1":
                        visited.add((row, col))
                        res.append((row, col))
            return res


        def bfs(row, col):
            cell = (row, col)
            queue = deque()
            queue.append(cell)
            visited.add(cell)

            while len(queue) > 0:
                curr = queue.popleft()
                r, c = curr
                for neighbor in get_neighbors(r, c):
                    visited.add(neighbor)
                    queue.append(neighbor)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cell = grid[row][col]
                if (row, col) not in visited and cell == "1":
                    # unexplored island
                    count += 1
                    bfs(row, col)  # marks every island block as visited
        return count