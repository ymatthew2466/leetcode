# 1052. Grumpy Bookstore Owner


from typing import List
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        '''
        slide window of size minutes across GRUMPY list

        find window where # of CHANGED customers is greatest (best window)

        add up all customers outside of window + inside of window

        when grumpy == 0, customer is valid
        '''

        # first window
        l = 0
        # window can't exceed array length
        r = minutes-1 if len(grumpy) > minutes else len(grumpy)-1
        max_change = 0
        max_index = 0
        for i in range(l, r+1):
            if grumpy[i] == 1:
                max_change += customers[i]
        # print(f"maximum cust changed: {max_change}")

        curr_change = max_change
        for i in range(1, len(grumpy)-minutes+1):
            prev = i-1
            right = i+minutes-1

            if grumpy[prev] == 1:
                curr_change -= customers[prev]
            if grumpy[right] == 1:
                curr_change += customers[right]
            
            if curr_change > max_change:
                max_change = curr_change
                max_index = i
            # max_change = max(curr_change, max_change)
        
        cust = 0
        for i in range(len(customers)):
            if i >= max_index and i < max_index + minutes:
                cust += customers[i]
            else:
                if grumpy[i] == 0:
                    cust += customers[i]
        # print(f"cust: {cust}")
        # print(f"max change: {max_change}, max index: {max_index}")
        return cust