# 3151. Special Array I

from typing import List
class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        isEven = nums[0] % 2 == 0
        for num in nums:
            if isEven:
                if num % 2 != 0:
                    return False
            else:
                if num % 2 == 0:
                    return False
            if isEven:
                isEven = False
            else:
                isEven = True
        return True