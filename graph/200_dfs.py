# 200. Number of Islands (DFS)


from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        def dfs:
            visit action
            mark current node as visited
            iterate thru neighbors:
                dfs(neighbor)
        '''
        visited = set()
        count = 0

        def get_neighbors(row,col):
            indices = [(row+1, col), (row-1,col), (row,col+1), (row,col-1)]
            res = []
            for index in indices:
                r,c = index
                if r>=0 and r<len(grid) and c>=0 and c<len(grid[0]):
                    if grid[r][c] == "1" and (r,c) not in visited:
                        res.append((r,c))
            return res

        def dfs(row, col):
            print(row,col)

            visited.add((row,col))
            neighbors = get_neighbors(row,col)
            for r,c in neighbors:
                dfs(r,c)
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "0" or (row,col) in visited:
                    continue
                # increment count when find new island
                count += 1
                dfs(row, col)
        return count