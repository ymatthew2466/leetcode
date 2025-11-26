# 658. Find K Closest Elements

from typing import List


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        '''
        binary search on starting position of k window

        If x is farther from left boundary, move window right
        else: consider positions to the left
        '''
        left, right = 0, len(arr) - k
        
        while left < right:
            mid = (left + right) // 2
            # Compare distances from window boundaries to x
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        
        return arr[left:left + k]
        
        # '''
        # len(window) = k

        # end conditions:
        #     1. if x is not in bounds, return window from that extreme side
        #     2. if elt in window, but either left/right window bound is touching edge, return
        #     3. else:
        #         - normal
        # '''
        # if x <= arr[0]:
        #     return arr[0:k]
        # if x > arr[-1]:
        #     return arr[(len(arr)-1)-k: len(arr)]
                
        # def closer(a, b):
        #     # true if A is closer than B to X
        #     if abs(a-x) < abs(b-x):
        #         return True
        #     if abs(a-x) == abs(b-x):
        #         return a < b
        #     if abs(a-x) > abs(b-x):
        #         return False
        
        # for left in range(len(arr)-k+1):
        #     right = left + k - 1
        #     nxt = right + 1
            
        #     # end condition 2
        #     if nxt >= len(arr):
        #         return arr[left: right+1]
            
        #     if not closer(arr[nxt], arr[left]):
        #         return arr[left: right+1]
        
        # # rightmost
        # return arr[len(arr) - k:]