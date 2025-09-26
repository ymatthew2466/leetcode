# 2300. Successful Pairs of Spells and Potions


from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        '''
        optimal runtime: O(n * log(m))
            - iterate thru spells (n)
            - binary search on potions (log(m))
                - sort potions (m log(m))
        


        low = 0
        high = len(potions)

        find first index in potions s.t. spell*potion >= success
        count how many to the right of that

        left condition:
            if spell * potion[i] >= success:
                return True
        '''
        potions.sort()  # O(M * logM)

        def condition(mid, spell):
            if spell * potions[mid] >= success:
                return True
            else:
                return False
        
        res = []
        # print(potions)
        for spell in spells:
            low = 0
            high = len(potions)
            while low < high:
                mid = low + (high-low)//2
                if spell * potions[mid] >= success:
                    high = mid
                else:
                    low = mid + 1
            if condition(mid, spell):
                res.append(len(potions)-low)
            else:
                res.append(0)
            # print(low)
        return(res)
        
