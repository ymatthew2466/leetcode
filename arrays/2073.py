# 2073. Time Needed to Buy Tickets

"""
Future direction:
Try again with O(N) implementation.
"""
from typing import List


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        '''
        need some way to identify K elt (not position-based)
        - conversely, we can shift K whenever a shuffle happens
        - or, create wrapper class and use type(), but might be cheating
        '''

        count = 0

        # accepts num_tix AFTER 1 is subtracted, shuffles K
        def shuffle(num_tix: int):
            # must declare as nonlocal to read out of scope
            nonlocal tickets, k, count 
            
            tickets.pop(0)
            if num_tix > 0:
                tickets.append(num_tix)
                # adjust K
                if k > 0:
                    k -= 1
                else:
                    k = len(tickets)-1
            else:
                if k > 0:
                    k -= 1
                else:
                    k = None
            count += 1
            
        while k != None:
            shuffle(tickets[0]-1)
        
        return count