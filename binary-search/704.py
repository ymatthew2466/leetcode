# 704. Binary Search

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = low + (high - low)//2
            elt = nums[mid]
            if elt == target:
                # if we find the element
                return mid
            elif elt < target:
                # if mid is smaller than target, focus on right side
                low = mid + 1
            elif elt > target:
                # if mid > target, focus on left side
                high = mid - 1
        return -1
            
            