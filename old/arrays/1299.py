# 1299. Replace Elements with Greatest Element on Right Side

from typing import List
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''
        <-- right to left <--

        maintain max up to that point
        set each index as max
        '''
        curr_max = arr[-1]
        for i in range(len(arr)-1, -1, -1):
            curr = arr[i]
            arr[i] = curr_max
            curr_max = max(curr_max, curr)
        arr[-1] = -1
        return arr