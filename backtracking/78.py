# 78. Subsets


from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        avoid checking duplicates (overcomplicate) by solving efficiently

        include curr_subset and start index at each recursion depth

        at every depth,
            - loop thru list, starting at index
                - prevents duplicates
                - append num at index
                - call backtrack
                - remove appended num to "reset" for next iteration
        '''
        res = []
        def recursive(curr_subset, start_index):
            res.append(curr_subset[:])

            # add to res
            for i in range(start_index, len(nums)):
                curr_subset.append(nums[i])
                recursive(curr_subset, i + 1)

                # essential backtrack step to undo the append (try next element)
                # basically, resets to diff "starter" values
                curr_subset.pop()
        
        recursive([], 0)
        return res