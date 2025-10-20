# 3442. Maximum Difference Between Even and Odd Frequency I

class Solution:
    def maxDifference(self, s: str) -> int:
        '''
        find highest odd frequency - lowest even frequency

        frequency array -> len=26
        '''
        def get_index(char): 
            return ord(char) - ord('a')
        
        freq = [0] * 26
        for char in s:
            index = get_index(char)
            freq[index] += 1
        
        max_odd = float('-inf')
        min_even = float('inf')
        for f in freq:
            # if even
            if f%2 == 0 and f > 0 and f < min_even:
                min_even = f
            elif f%2 != 0 and f > 0 and f > max_odd:
                max_odd = f
        return max_odd-min_even
                