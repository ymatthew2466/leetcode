class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        track cheapest price, up to i
        track most profit, up to i
        '''
        lowest = float('inf')
        profit = float('-inf')
        for i in range(len(prices)):
            price = prices[i]
            lowest = min(price, lowest)
            profit = max(profit, price-lowest)
        return profit