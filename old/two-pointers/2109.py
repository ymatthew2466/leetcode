# 2109. Adding Spaces to String


from typing import List
class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # everytime we add a space, we need to account for index offset
        offset = 0

        '''
        ptr1 inside s
        ptr2 inside spaces
        '''
        res = ""
        ptr2 = 0
        for i in range(len(s)):
            char = s[i]
            if ptr2 < len(spaces) and spaces[ptr2] == i:
                res += " "
                ptr2 += 1
            res += char
        return res
        