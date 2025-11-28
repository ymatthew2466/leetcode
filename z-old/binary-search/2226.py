# 2226. Maximum Candies Allocated to K Children


from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        '''
        low: 0
        high: max(candies)

        guess # candies per child -> output k_guess
        
        if k_guess > k:
            we can feed too many kids (so increase candies)
            candies up, so look right
        if k_guess < k:
            too many candies per kid
            reduce candies to increase kids
            <= checks if we serve K OR FEWER kids, but we want AT LEAST K kids, so <
            return True
        
        algo to calculate k:
        def calc_k(guess):
        
        return low-1 bc we find first value that's too large, 
            so return first valid (-1 of that)
        '''                

        def calc_k(guess) -> int:
            k_guess = 0
            for pile in candies:
                k_guess += pile//guess
            return k_guess
        
        def condition(guess):
            k_guess = calc_k(guess)
            if k_guess < k:
                return True
            else:
                return False
    
        low = 1
        high = max(candies)+1
        
        while low < high:
            mid = low + (high-low)//2
            if condition(mid):
                high = mid
            else:
                low = mid + 1
        
        return low-1