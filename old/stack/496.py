# 496. Next Greater Element I


from typing import List
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''
        * distinct numbers
        iterate thru nums 2 and create dict
        K: number (not index), V: next greatest
        iterate right <-- left
        maintain stack of decreasing elements
        '''
        stack = []
        d = {}
        for i in range(len(nums2)-1, -1, -1):
            curr = nums2[i]
            
            # pop elements <= current
            while stack and stack[-1] <= curr:
                stack.pop()
            
            # next greater element top of stack or -1
            d[curr] = stack[-1] if stack else -1
            stack.append(curr)
        
        res = []
        for i in range(len(nums1)):
            res.append(d[nums1[i]])
        return res