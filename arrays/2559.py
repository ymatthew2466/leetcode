# 2559. Count Vowel Strings in Ranges


from typing import List
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        '''
        use prefix sums
            - prefix[i] is num of valid words, from index 0 to i-1
            - to find num in range [l, r], we do prefix[r+1] - prefix[l]

        words = ["aba", "bcb", "ece"]  
        prefix_sum = [0, 1, 1, 2]
        '''
        vowels = {'a', 'e', 'i', 'o', 'u'}
        count = 0
        prefix_sum = [0]
        for i in range(len(words)):
            word = words[i]
            if word[0] in vowels and word[-1] in vowels:
                count += 1
                prefix_sum.append(count)
            else:
                prefix_sum.append(count)

        res = []
        for query in queries:
            l = query[0]
            r = query[1]
            res.append(prefix_sum[r+1]-prefix_sum[l])
        return(res)


        # '''
        # iterate thru words
        #     if word is valid, add index to set
        
        # iterate thru queries
        #     if any of indices in list is in set, count += 1
        # '''
        # vowels = {'a', 'e', 'i', 'o', 'u'}
        # vowel_strings = set()
        # for i in range(len(words)):
        #     word = words[i]
        #     if word[0] in vowels and word[-1] in vowels:
        #         vowel_strings.add(i)
        
        # res = []
        # for query in queries:
        #     count = 0
        #     for i in range(query[0], query[1]+1):
        #         if i in vowel_strings:
        #             count += 1
        #     res.append(count)
        # return(res)