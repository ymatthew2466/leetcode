class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        '''
        bfs on grid2
        if island, we build out the island using BFS
        check each index against grid1 to ensure it's also 1
        if there's '1' in grid2 but not in grid1, then false

        '''
        visited = set()

        def get_neighbors(r, c):
            indices = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            res = []
            for r1, c1 in indices:
                if r1 >= 0 and r1 < len(grid2) and c1 >= 0 and c1 < len(grid2[0]):
                    if (r1, c1) not in visited and grid2[r1][c1] == 1:
                        res.append((r1, c1))
            return res

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            isSub = True

            while len(q)>0:
                curr = q.popleft()
                r1, c1 = curr

                # condition
                if grid1[r1][c1] != 1:
                    isSub = False

                for r2, c2 in get_neighbors(r1, c1):
                    q.append((r2, c2))
                    visited.add((r2, c2))
            return isSub

        count = 0
        for row in range(len(grid2)):
            for col in range(len(grid2[0])):
                if (row, col) not in visited and grid2[row][col] == 1:
                    if bfs(row, col):
                        print(row, col)
                        count += 1
        return count