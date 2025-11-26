class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        check if same number of letters in both words
        '''
        if len(s) != len(t):
            return False
        s_d = {}
        t_d = {}
        for i in range(len(s)):
            s_letter = s[i]
            t_letter = t[i]
            s_d[s_letter] = s_d.get(s_letter, 0) + 1
            t_d[t_letter] = t_d.get(t_letter, 0) + 1
        if s_d == t_d:
            return True
        return False