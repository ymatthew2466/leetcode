# 290. Word Pattern


from typing import List
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False
        for i in range(len(pattern)):
            pattern_letter = pattern[i]
            s_letter = s_list[i]
            if pattern_letter not in dic:
                if s_letter in dic.values():
                    return False
                dic[pattern_letter] = s_letter
            
            if s_letter != dic[pattern_letter]:
                print(s_letter, dic[pattern_letter])
                return False
            print(s_letter, dic[pattern_letter])
        return True
                