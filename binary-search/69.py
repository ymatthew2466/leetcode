# 69. Sqrt(x)

class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        condition for first valid case:
            if num*num >= x:
                if square is greater than x, we need to narrow down on the left
                return True
            if num*num < x:
                if square is less than x, find bigger values to the right
                return False
        '''
        def condition(mid):
            if mid*mid >= x:
                return True
            else:
                return False
        
        low = 1
        high = x+1
        
        while low < high:
            mid = low + (high-low)//2
            if condition(mid):
                high = mid
            else:
                low = mid + 1
        if low*low > x:
            return low-1
        else:
            return low