# 438. Find All Anagrams in a String


from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        '''
        convert p into dict -- k: char, v: frequency

        make the window len(p)
        
        for i in range(len(s)-len(p)):
            take the substring in the window and convert to dict
            check equivalency to p_dict
        '''
        if len(p) > len(s): 
            return []

        # convert string to frequency array (index 0 = a, value = frequency)
        def to_array(st: str):
            arr = [0] * 26
            for char in st:
                index = ord(char) - ord('a')
                arr[index] += 1
            return arr


        p_arr = to_array(p)
        res = []
        window = len(p)
        window_str = s[0: len(p)]
        window_arr = to_array(window_str)

        # hardcode first index
        if window_arr == p_arr:
            res.append(0)

        for i in range(1, len(s)-len(p)+1):
            # remove char from frequency arr
            char = s[i-1]
            index = ord(char) - ord('a')
            window_arr[index] -= 1

            # add rightmost char of window
            char2 = s[i + window - 1]
            index2 = ord(char2) - ord('a')
            window_arr[index2] += 1

            if window_arr == p_arr:
                res.append(i)
        
        return res