# 1984. Minimum Difference Between Highest and Lowest of K Scores


from typing import List
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        '''
        find window where max-min is minimized

        1,4,7,9

        start by sorting array
            - the smallest difference will never be outside the sliding window

        slide the window, check right-left and keep track of minimum

        window = k
        '''
        if k == 1:
            return 0
        
        mini = float('inf')
        nums = sorted(nums)
        for i in range(len(nums)-k+1):
            left = nums[i]
            right = nums[i+k-1]
            mini = min(mini, right-left)
            # print(f"left: {i}, right: {i+k}, substr: {nums[i:i+k]}")
            # print(f"mini: {mini}")
        return mini