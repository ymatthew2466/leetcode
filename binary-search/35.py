# 35. Search Insert Position

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        def condition(mid):
            # condition for first valid index
            return nums[mid] >= target
        
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right-left)//2

            if condition(mid):
                # what we have is valid, look at left to narrow it down
                right = mid
            else:
                # invalid and everything to left is invalid, look at right
                left = mid + 1
        return left