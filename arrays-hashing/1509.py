# 1509. Minimum Difference Between Largest and Smallest Value in Three Moves


from typing import List
class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        '''
        sort array

        to close the gap, we need to remove elements at the ends

        combinations:
            1. remove 3 biggest
            2. remove 3 smallest
            3. remove 2 big/1 small
            4. remove 1 big/2 small
        
        '''
        nums.sort()
        rm3biggest = nums[-4] - nums[0]
        rm3smallest = nums[-1] - nums[3]
        rm2big1small = nums[-3] - nums[1]
        rm1big2small = nums[-2] - nums[2]
        return min(rm3biggest, rm3smallest, rm2big1small, rm1big2small)