# 540. Single Element in a Sorted Array


from typing import List
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        ANALYZE THE LENGTH OF EACH SIDE, DEPENDING ON WHICH DOUBLE IT IS
            - IF THERE'S ONLY 1 OF ELEMENT, WE KNOW THAT SIDE ODD LENGTH!!
        
        when to look mid+left?
            - left (including mid) has odd number of elts
            - cut off s.t. includes (if pointer at 1 of 2 digit, cut off including that)
        when to look right?
            - left has even number of elts

        def condition(curr):
            if nums[curr] != nums[curr+1]:
                # we're on first digit -> ignore, and only look at second
            
            if right side (excluding curr) even, answer must be CURR or LEFT
        '''
        def condition(curr):
            if curr<len(nums)-1 and nums[curr] == nums[curr+1]:
                # if we're at first dig, only consider second
                curr += 1
            # if right side (excluding curr) is even, answer must be on left (including curr)
            if len(nums[curr+1:]) % 2 == 0:
                return True
            else:
                return False
        
        low = 0
        high = len(nums)+1
        while low<high:
            mid = low + (high-low)//2
            if condition(mid):
                # look left
                high = mid
            else:
                # look right
                low = mid + 1
        return nums[low]



