# 49. Group Anagrams

from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        - anagram = same number of each char
        - convert to list of dictionaries (same index as og list)
            - k: letter, v: frequency
            - check if word_dict1==word_dict2, if true, anagram
        
        - sort into buckets based on dictionary
        '''

        def make_word_dict(s: str):
            d = {}
            for char in s:
                # increment count for char
                d[char] = d.get(char, 0) + 1
            return d

        list_word_dict = []
        for i in range(len(strs)):
            word = strs[i]
            word_dict = make_word_dict(word)
            list_word_dict.append((word_dict, word))
        
        buckets = {}
        for d, word in list_word_dict:
            normalized_key = tuple(sorted(d.items()))
            if normalized_key not in buckets:
                buckets[normalized_key] = []
            buckets[normalized_key].append(word)
        res = list(buckets.values())
        return res
