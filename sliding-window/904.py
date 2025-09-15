# 904. Fruit Into Baskets

from typing import List
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        sliding window

        dict -- K: fruit type, V: count

        expand window right as long as possible while 2 unique fruits

        if 3 unique fruits: 
            shrink left until 2 unique fruits again
            delete stuff from dict
        '''
        counts = {}
        left = 0
        max_window = 0
        for right in range(len(fruits)):
            fruit = fruits[right]
            counts[fruit] = counts.get(fruit, 0) + 1  # increment
            
            # more than 2 unique fruits, shrink window
            while len(counts) > 2:
                left_fruit = fruits[left]
                counts[left_fruit] -= 1
                if counts[left_fruit] == 0:
                    del counts[left_fruit]
                left += 1
            window_size = right-left + 1
            max_window = max(max_window, window_size)
        return max_window
