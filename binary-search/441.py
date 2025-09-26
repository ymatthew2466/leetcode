#441. Arranging Coins


class Solution:
    def arrangeCoins(self, n: int) -> int:
        '''
        low = 0 rows
        high = n rows

        e.g.
        4 rows -> 1+2+3+4 expected coins

        USE: row * (row + 1) / 2

        '''
        
        def condition(mid):
            coins = mid * (mid+1)/2
            if coins > n:
                return True
            else:
                return False

        low = 0
        high = n+1
        while low < high:
            mid = low + (high-low)//2
            if condition(mid):
                high = mid
            else:
                low = mid + 1
        if low*(low+1)/2 == n:
            return low
        return low-1
