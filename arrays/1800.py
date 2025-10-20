# 1800. Maximum Ascending Subarray Sum

from typing import List
class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        '''
        reset total if ascending is interrupted

        maintain max
        '''

        total = nums[0]
        mx = nums[0]

        for i in range(1, len(nums)):
            prev = nums[i-1]
            curr = nums[i]
            if curr <= prev:
                total = curr
            else:
                total += curr
            mx = max(mx, total)
        return mx