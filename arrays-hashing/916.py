# 916. Word Subsets

from typing import List
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        '''
        word1 must be a subset of ALL word2
            - only consider most strict requirement for each char
            - if 'c' and 'cc', so word1 must contain 2 c's
            - convert words2 to max freq array
        
        for word1 in words1:
            make freq array
            iterate thru word1 freq array:
                check if each count >= max freq array

        '''
        def get_index(ch):
            return ord(ch) - ord('a')

        max_freq = [0] * 26
        for word2 in words2:
            freq = [0] * 26
            for char in word2:
                index = get_index(char)
                freq[index] += 1
            # update max freq
            for i in range(len(max_freq)):
                max_freq[i] = max(max_freq[i], freq[i])
        
        res = []
        for word1 in words1:
            freq = [0] * 26
            for char in word1:
                index = get_index(char)
                freq[index] += 1
            valid = True
            for i in range(len(freq)):
                if freq[i] < max_freq[i]:
                    valid = False
            if valid:
                res.append(word1)
        return(res)