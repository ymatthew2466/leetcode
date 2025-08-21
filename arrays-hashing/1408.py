# 1408. String Matching in an Array

from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        '''
        criteria to determine if word is substring:
        1. len(sub) <= len(word)
        2. O(N^2) approach is pretty easy
        3. the substring might appear BEFORE the actual word
        4. brute force
        ...
        FOR THE FUTURE, try KMP algorithm
        '''

        def is_substr(substring, complete):
            for i in range(len(complete)-len(substring)+1):
                char = complete[i]
                # at each char, take next len(substring) chars and check if equal
                if complete[i: i+len(substring)] == substring:
                    return True
            return False

        res = set()
        for i in range(len(words)):
            for j in range(len(words)):
                # can't compare to itself
                if i == j:
                    continue
                substring = words[i]
                complete = words[j]

                # substr must be <= word
                if len(substring) > len(complete):
                    continue
                if is_substr(substring, complete):
                    res.add(substring)
        return list(res)
                
                