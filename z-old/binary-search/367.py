# 367. Valid Perfect Square

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        '''
        low = 1, high = num + 1

        condition of first valid element: if mid * mid >= num
            it is valid, so look left to narrow it down
        

        '''
        def condition(mid):
            return mid * mid >= num

        low = 1
        high = num+1
        while low < high:
            mid = low + (high-low)//2
            # print(low, mid, high, condition(mid))

            if condition(mid):
                # look left
                high = mid
            else:
                # look right
                low = mid + 1
        return low*low==num
        
