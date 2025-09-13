# 130. Surrounded Regions


from collections import deque
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        '''
        2 approaches:
            - ignore borders and BFS every interior cell to see if any O areas spill into borders
            - ONLY look at borders and BFS every O cell

        if outer cell not visited and == 'O':
            bfs
        
        while 
        '''
        if len(board) <= 1 or len(board[0]) <= 1:
            return
        
        visited = set()
        safe = set()
        
        def get_neighbors(r, c):
            indices = [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]
            res = []
            for r1, c1 in indices:
                if (r1, c1) not in visited:
                    if r1 >= 0 and r1 < len(board) and c1 >= 0 and c1 < len(board[0]):
                        if board[r1][c1] == "O":
                            res.append((r1,c1))
            return res

        def bfs(r, c):
            q = deque()
            q.append((r,c))
            visited.add((r,c))
            while len(q)>0:
                curr = q.popleft()
                # visited.add(curr)  # REDUNDANT
                safe.add(curr)  # add border-touching O's to safe
                for neighbor in get_neighbors(curr[0], curr[1]):
                    q.append(neighbor)
                    visited.add(neighbor)
                    safe.add(neighbor)  # add neighbor 0's to safe


        for row in range(len(board)):
            for col in range(len(board[0])):
                if row!=0 and row!=len(board)-1 and col!=0 and col!=len(board[0])-1:
                    # not a border cell
                    continue
                # bfs "O" border cells
                if (row, col) not in visited and board[row][col] == "O":
                    bfs(row, col)  # marks all safe cells
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if (row, col) in safe or board[row][col]=="X":
                    continue
                board[row][col] = "X"