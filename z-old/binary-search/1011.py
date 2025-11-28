# 1011. Capacity To Ship Packages Within D Days


from typing import List
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        binary search for max weight
        low: 1
        high: sum(weights)

        at each guess:
            calculate days
        
        def calc_days(guess):
            curr_weight = 0
            days = 0
            for weight in weights:
                if curr_weight > guess:
                    add day
                    reset curr_weight


        LEFT CONDITION:
            if days_guess <= days:
                we can use more days and reduce the max weight
        
        '''
        def calc_days(max_weight):
            curr = 0
            days_t = 1
            for weight in weights:
                curr += weight
                if curr > max_weight:
                    days_t += 1
                    curr = weight
            return days_t
        
        def condition(mid):
            days_t = calc_days(mid)
            if days_t <= days:
                return True
            else:
                return False

        low = max(weights)
        high = sum(weights)
        while low < high:
            mid = low + (high-low)//2
            if condition(mid):
                high = mid
            else:
                low = mid + 1
        return low
        