# 3110. Score of a String

class Solution:
    def scoreOfString(self, s: str) -> int:
        '''
        ord(char) to get ASCII

        iterate thru and maintain count
        '''
        
        count = 0
        for i in range(len(s) -1):
            curr = ord(s[i])
            nxt = ord(s[i+1])
            diff = abs(curr - nxt)
            count += diff
        return count