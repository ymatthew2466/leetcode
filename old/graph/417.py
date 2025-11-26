# 417. Pacific Atlantic Water Flow


from typing import List
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        BFS

        start from ocean cells (pacific and atlantic separately)
        run BFS on edge cells to find cells that can flow into THAT ocean

        return union of pacific and atlantic BFS
        '''

        pacset, atlset = set(), set()
        pacres, atlres = [], []

        def get_neighbors(r, c):
            indices = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            res = []
            for r1, c1 in indices:
                if r1 >= 0 and r1 < len(heights) and c1 >= 0 and c1 < len(heights[0]):
                    if heights[r1][c1] >= heights[r][c]:
                        res.append((r1, c1))
            return res

        def bfs(r0, c0, isPAC):
            nonlocal pacset, atlset
            res = []
            q = deque()
            visited = pacset if isPAC else atlset
            q.append((r0, c0))
            visited.add((r0, c0))
            while len(q)>0:
                curr = q.popleft()
                r1, c1 = curr

                # add to res
                res.append(curr)

                for neighbor in get_neighbors(r1, c1):
                    if neighbor not in visited:
                        q.append(neighbor)
                        visited.add(neighbor)
            if isPAC:
                pacset = visited
            else:
                atlset = visited
            return res


        # iterate thru pac cells
        # top row
        for i in range(len(heights[0])):
            cell = (0, i)
            row, col = cell
            if cell not in pacset:
                pacres.extend(bfs(row, col, True))
            
        # left col
        for i in range(len(heights)):
            cell = (i, 0)
            row, col = cell
            if cell not in pacset:
                pacres.extend(bfs(row, col, True))
        
        # atl cells
        # bot row
        for i in range(len(heights[0])):
            cell = (len(heights)-1, i)
            row, col = cell
            if cell not in atlset:
                atlres.extend(bfs(row, col, False))
        
        # right col
        for i in range(len(heights)):
            cell = (i, len(heights[0])-1)
            row, col = cell
            if cell not in atlset:
                atlres.extend(bfs(row, col, False))

        return list(set(atlres) & set(pacres))