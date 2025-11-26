# 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold


from typing import List
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        '''
        sliding window of size K

        init window from 0 to K, calculate average

        iterate thru list(start index==1, until len(arr)-k+1):
            - remove prev element
            - add right element
            - calculate average dynamically
            - if avg > threshold, append sublist

        '''
        count = 0

        # init window and avg
        # init = arr[0:k]
        avg = sum(x for x in arr[0:k])/k

        # append first window case
        if avg >= threshold:
            count += 1
        
        for i in range(1, len(arr)-k+1):
            # avg -= (init.pop(0)/k)
            # avg += (arr[i+k-1]/k)
            # init.append(arr[i+k-1])

            avg -= arr[i-1]/k  # remove prev left from avg
            avg += arr[i+k-1]/k  # add new right to avg
            if avg >= threshold:
                count += 1
        return count