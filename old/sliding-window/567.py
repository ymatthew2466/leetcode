# 567. Permutation in String


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        convert s1 to dict 
            K: letter, V: frequency
        
        window = len(s1)

        1. build the first dict starting at index 0
        2. iterate thru s2:
            - remove left char from dict
            - add right char from dict
            - check equivalency to s1_dict
        '''
        if len(s1) > len(s2):
            return False
        
        # set up s1_dict, and first window for s2
        s1_dict = {}
        s2_dict = {}
        for i in range(len(s1)):
            s1_char = s1[i]
            s1_dict[s1_char] = s1_dict.get(s1_char, 0) + 1

            s2_char = s2[i]
            s2_dict[s2_char] = s2_dict.get(s2_char, 0) + 1
        
        # check first window
        if s1_dict == s2_dict:
            return True
        
        for i in range(1, len(s2)-len(s1)+1):
            left_prev = s2[i-1]
            right = s2[i+len(s1)-1]
            
            # fade the prev left char
            s2_dict[left_prev] -= 1
            if s2_dict[left_prev] == 0:
                s2_dict.pop(left_prev)

            # add new right char
            s2_dict[right] = s2_dict.get(right, 0) + 1
            
            if s1_dict == s2_dict:
                return True

            # print(f"s1: {s1_dict}, s2: {s2_dict}")
            
        return False
