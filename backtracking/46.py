# 46. Permutations


from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        iterate thru nums:
            - each elt is a starter
                - fed into recursive function
        
        def recursive(string: len(string) < len(nums), list without dupes):
            base case: len(str) == len(nums)
                - done
            recursive case:
                - for num in list:
                    - recursive(str + num, list.remove(num))
        '''
        nset = set()
        for num in nums:
            nset.add(num)
        
        res = []
        def recursive(s: list, available: set):
            if len(s) == len(nums):
                # no more numbers to add
                res.append(s)
                return
            for num in available:
                temp = available.copy()
                temp.remove(num)

                temp_list = s.copy()
                temp_list.append(num)
                recursive(temp_list, temp)
        
        for num in nset:
            temp = nset.copy()
            temp.remove(num)
            recursive([num], temp)
        
        return(res)
