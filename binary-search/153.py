# 153. Find Minimum in Rotated Sorted Array


from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        condition for splitting:
        left case:
            if nums[low] > curr OR nums[low]<nums[high]:
                left
            elif nums[low] <= curr:
                right
        
        [4,5,6,7,8,1,2,3]
               ^
        [7,8,1,2,3,4,5,6]
               ^
        [1,2,3,4,5,6,7,8]
               ^

        '''
        low = 0
        high = len(nums)

        def condition(mid):
            high_t = high-1 if high==len(nums) else high
            if nums[low] > nums[mid] or nums[low] < nums[high_t]:
                return True
            else:
                return False
        
        while low<high:
            mid = low + (high-low)//2
            if condition(mid):
                high = mid
            else:
                low = mid + 1
        if low >= len(nums):
            return nums[-1]
        if low < 0:
            return nums[0]
        return nums[low]