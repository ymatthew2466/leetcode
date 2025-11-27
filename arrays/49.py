class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        make an array len=26 for each letter 
        each anagram will have SAME ARRAY
        convert to tuple and store in dict
        K: array tuple, V: [words]
        
        '''
        d = {}
        for word in strs:
            chars = [0]*26
            for char in word:
                chars[ord(char)-ord('a')] += 1
            tup = tuple(chars)
            val = d.get(tup, [])
            val.append(word)
            d[tup] = val
        res = []
        for key in d:
            res.append(d[key])
        return res