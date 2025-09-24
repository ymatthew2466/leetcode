# 74. Search a 2D Matrix


from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        convert flat index to (row, col):
            row = floor(index / cols)
            col = index % cols

        low = 0
        high = total # elts + 1

        def condition(mid):

            row, col = convert(mid)
            left condition -> if matrix[row,col] <= target: True
        '''

        rows = len(matrix)
        cols = len(matrix[0])
        
        # 0-based
        def flat_to_rowcol(index):
            row = index // cols
            col = index % cols
            return (row, col)

        def condition(mid):
            row, col = flat_to_rowcol(mid)
            # left condition
            if matrix[row][col] >= target:
                return True
            else:
                return False
        
        low = 0
        high = rows*cols
        while low<high:
            mid = low + (high-low)//2
            print(f"low: {low}, mid: {mid}, high: {high}, mid_grid: {flat_to_rowcol(mid)}")
            if condition(mid):
                high = mid
            else:
                low = mid + 1
        row, col = flat_to_rowcol(low)
        if row >= 0 and row < rows and col >= 0 and col < cols:
            return matrix[row][col] == target
        else:
            return False