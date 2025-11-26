# 121. Best Time to Buy and Sell Stock


from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        keep track of:
            - cheapest day
            - best profit
        '''

        cheapest = float('inf')
        best = float('-inf')

        for i in range(len(prices)):
            if prices[i] < cheapest:
                cheapest = prices[i]
            if prices[i] - cheapest > best:
                best = prices[i]-cheapest
        return best


'''
version that exceeds time limits and overcomplicated but works and I spent lots of time on it
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        [day1: day2] is window

        When to shrink/expand window?
        Buy at low price, sell at high price

        [7,3,5,1,6,4]
        
        0-0: 0
        0-1: -4
        0-2: -2 (local max, so shrink left)
        1-2: 2 (local max)
        1-3: -2
        1-4: 3 (local max)

        keep sliding window right, if we find a local max, try shrinking left until l==r-1.
            if there's a window where we get new local max, set window, then keep growing right

        if right pointer gets to end of array, if no local max, break
        '''
        if len(prices) <= 1: 
            return 0
        
        l, r = 0, 0
        best = float("-inf")
        bl, br = 0, 0

        while r<len(prices):
            curr = prices[r]-prices[l]


            # new best price
            if curr > best:
                # set window
                bl, br = l, r
                best = curr

            temp_l = l
            # try shrinking left as much as possible to see if we get a new max
            while temp_l<r:
                temp_l += 1
                # found a new left within the window that's better
                if prices[r]-prices[temp_l] > best:
                    bl = temp_l
                    best = prices[r]-prices[temp_l]
                    l= temp_l
            
            r += 1
        return best if best>0 else 0