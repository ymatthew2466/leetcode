# 374. Guess Number Higher or Lower


# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int: ...

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # setup template
        def condition(mid):
            # out = False
            if guess(mid) == 0 or guess(mid) == -1:
                return True
        
        left = 1
        right = n+1

        while left < right:
            mid = left + (right-left)//2
            
            if condition(mid):
                # mid satifies, find better solution on the left
                right = mid
            else:
                # does not satisfy, find solution on right
                left = mid + 1
        return left

