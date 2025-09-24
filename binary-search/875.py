# 875. Koko Eating Bananas


from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        low = 1
        high = max(piles)

        how do we know lower/higher of curr guess?
            iterate thru arra
                calculate H, given K from binary search guess
                if H > h, need a HIGHER K value, so look right
                if H <= h, need a LOWER K value, so look left

        O(n*log(n))

        def calculate_h(k):
            count = 0
            iterate thru arr:
                hours needed = math.ceil(element/k)
                count += hours needed

        '''
        def calculate_h(speed):
            count = 0
            for elt in piles:
                hours_needed = math.ceil(elt/speed)
                count += hours_needed
            return count
        
        def condition(mid):
            h_prime = calculate_h(mid)
            if h_prime <= h:
                return True  # look left 
            else:
                return False
        
        low = 1
        high = max(piles)+1
        while low < high:
            mid = low + (high-low)//2
            if condition(mid):
                high = mid
            else:
                low = mid + 1
        return(low)

