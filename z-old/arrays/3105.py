#3105. Longest Strictly Increasing or Strictly Decreasing Subarray

from typing import List
class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        '''
        if we switch between increasing/decreasing:
            increment by 1 AND set other to 1
        
        maintain max
        '''
        if len(nums)<=1:
            return len(nums)

        inc = 1
        dec = 1
        mx = float("-inf")

        for i in range(1, len(nums)):
            prev = nums[i-1]
            curr = nums[i]
            if curr > prev:  # increasing
                inc += 1
                dec = 1
            elif curr < prev:  # decreasing
                dec += 1
                inc = 1
            else:  # equal
                inc = 1
                dec = 1
            mx = max(mx, inc, dec)
        return mx