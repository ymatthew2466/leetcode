# 733. Flood Fill


from collections import deque
from typing import List
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        '''
        bfs

        visit set
        deque()
        popleft

        while queue:
            curr = popleft
            add curr to visit
            change color
            for neighbor of curr:
                if neighbor not visited:
                    add to queue
                    add to visited
        '''
        start = image[sr][sc]
        def get_neighbors(curr):
            r,c = curr
            indicies = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            res = []
            # edge cases
            for row, col in indicies:
                if row >= 0 and row < len(image) and col >= 0 and col < len(image[0]):
                    if image[row][col] == start:
                        res.append((row, col))
            return res

        
        visited = set()
        queue = deque()
        queue.append((sr, sc))
        while queue:
            curr = queue.popleft()
            visited.add(curr)
            # change color
            r, c = curr
            image[r][c] = color
            # get neighbors
            for neighbor in get_neighbors(curr):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return image
