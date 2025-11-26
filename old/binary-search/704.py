# 704. Binary Search


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def condition(value) -> bool:
            return nums[value] >= target

        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1
        
        # ensure that the index where condition becomes true (nums[index] >= target)
        # is actually equal to target (nums[index] == target)
        if left >= 0 and left < len(nums) and nums[left] == target:
            return left
        return -1


# from typing import List

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         low = 0
#         high = len(nums)-1
#         while low <= high:
#             mid = low + (high - low)//2
#             elt = nums[mid]
#             if elt == target:
#                 # if we find the element
#                 return mid
#             elif elt < target:
#                 # if mid is smaller than target, focus on right side
#                 low = mid + 1
#             elif elt > target:
#                 # if mid > target, focus on left side
#                 high = mid - 1
#         return -1
            
            