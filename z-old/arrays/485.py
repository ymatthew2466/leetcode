# 485. Max Consecutive Ones


from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxi = 0
        for elt in nums:
            if elt == 1:
                count += 1
            else:
                count = 0
            
            if count >= maxi:
                maxi = count

        return maxi