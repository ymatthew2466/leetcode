# 162. Find Peak Element


from typing import List
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        what condition marks the first valid index:
            elt > elt[mid-1] or mid == -1
            and
            elt > elt[mid+1] or mid+1 == n

        when go left? when go right?

        [(4), 2] -> if elt to the right is equal/lower, peak could be curr OR left
        [(3), 5] -> if elt to the right is greater, peak is to the right
        '''
        
        def condition(curr):
            # when to go left
            if curr == len(nums)-1 or nums[curr] >= nums[curr+1]:
                return True
            elif curr == 0 or nums[curr] < nums[curr+1]:
                return False

        low = 0
        high = len(nums)
        count = 0
        while low < high and count < 10:
            mid = low + (high-low)//2
            
            if condition(mid):
                print(f"left: {low}, {mid}, {high}")
                high = mid
            else:
                print(f"right: {low}, {mid}, {high}")
                low = mid + 1
            count += 1
        return low